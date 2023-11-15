import datetime
from azure.storage.blob.aio import BlobServiceClient, BlobClient
from azure.storage.blob import (
    BlobServiceClient,
    BlobSasPermissions,
    generate_blob_sas,
)
from llama.program.util.config import get_config
import asyncio
import json
import hashlib
import os
import jsonlines

class AzureBlobClient:
    def __init__(self):
        self.config = get_config()
        self.container_client = self.get_client()

    def get_client(self):
        blob_service_client = BlobServiceClient.from_connection_string(
            conn_str=self.config["azure"]["azure_blob"]["connection_string"]
        )
        container_client = blob_service_client.get_container_client(
            self.config["azure"]["azure_blob"]["container_name"])
        return container_client

    def create_service_sas_blob(self, azure_dir_name, filename: str):
        start_time = datetime.datetime.now(datetime.timezone.utc)
        expiry_time = start_time + datetime.timedelta(days=self.config["azure"]["azure_blob"]["sas_expiry_days"])

        blob_client = self.container_client.get_blob_client(f"{azure_dir_name}/{filename}")

        sas_token = generate_blob_sas(
            account_name=blob_client.account_name,
            container_name=blob_client.container_name,
            blob_name=f"{azure_dir_name}/{filename}",
            account_key=self.config["azure"]["azure_blob"]["account_key"],
            permission=BlobSasPermissions(read=True, add=True, create=True, write=True),
            expiry=expiry_time,
            start=start_time
        )
        sas_url = f"{blob_client.url}?{sas_token}"
        print(f"Generated SAS URL: {sas_url}")
        blob_client_sas = BlobClient.from_blob_url(blob_url=sas_url)
        return blob_client_sas

    async def __upload_to_blob(self, blob_client_sas, data: str):
        async with blob_client_sas as blob:
            if await blob.exists():
                print(f"File/data already exists")
                url = blob_client_sas.url

            else:
                print("Uploading data....")
                await blob.upload_blob(data, blob_type="AppendBlob")
                print(f"Upload to blob completed for data.")
                url = blob.url
            url = url.split("?")[0]
            return url

    def upload_to_blob(self, azure_dir_name, filename, data: str):
        '''
        dir_name: dir name from root in blob storage where to upload this
        filepath: local file path of the file to upload
        '''

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            blob_client_sas = self.create_service_sas_blob(azure_dir_name, filename)
            tasks = [loop.create_task((self.__upload_to_blob(blob_client_sas, data)))]
            done, pending = loop.run_until_complete(asyncio.wait(tasks))
            results = []
            for future in done:
                url = future.result()
                results.append(url)
            return results[0]
        except Exception as e:
            print(f"\n\nError while running async upload task for file/data.")
            raise e
        finally:
            loop.close()


def upload_file_azure(filepath, azure_dir_name):
    with open(filepath, "r", encoding='utf-8') as f:
        data = json.loads(f.read())
    f.close()
    return upload_data_azure(data, azure_dir_name)


def upload_data_azure(data, azure_dir_name):
    client = AzureBlobClient()
    dataset_id = get_dataset_name(data)
    filename = f"{dataset_id}.jsonlines"
    return client.upload_to_blob(azure_dir_name, filename, json.dumps(data))


def upload_file_local(local_filepath, upload_base_path):
    """Read file at local_filepath and upload to upload_base_path"""
    data = []
    with open(local_filepath, "r", encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return upload_data_local(data, upload_base_path)


def upload_data_local(data, upload_base_path):
    dataset_id = get_dataset_name(data)
    upload_path = os.path.join(upload_base_path, str(dataset_id)) + ".jsonlines"
    if os.path.exists(upload_path):
        print(f"File/data already exists")
    else:
        with jsonlines.open(upload_path, "w") as f:
            f.write_all(data)
    return upload_path


def get_dataset_name(dataset):
    m = hashlib.sha256()
    m.update(str(dataset).encode("utf-8"))
    return m.hexdigest()

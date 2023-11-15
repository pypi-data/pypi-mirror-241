import config
import os

global_config = None


def get_config():
    global global_config
    assert global_config is not None
    return global_config


def setup_config(dictionary={}):
    global global_config
    global_config = config.ConfigurationSet(
        config.config_from_dict(dictionary),
        config.config_from_env(prefix="POWERML", separator="__", lowercase_keys=True),
        home_yaml_config()
    )

    config_paths = get_config_paths()

    for path in config_paths:
        global_config.update(config.config_from_yaml(path, read_from_file=True))

    global_config.update(
        config.config_from_env(prefix="LLAMA", separator="_", lowercase_keys=True)
    )

    return global_config

def get_config_paths():
    paths = []

    config_name = "llama_config"

    config_base = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "configs"
    )

    base_config_path = os.path.join(config_base, config_name + ".yaml")
    if os.path.exists(base_config_path):
        paths.append(base_config_path)

    local_config_path = os.path.join(config_base, config_name + "_local.yaml")
    if os.path.exists(local_config_path):
        paths.append(local_config_path)

    home = os.path.expanduser("~")
    home_config_path = os.path.join(home, "." + config_name + ".yaml")
    if os.path.exists(home_config_path):
        paths.append(home_config_path)

    return paths

def reset_config():
    global global_config
    global_config = None


def edit_config(dictionary={}):
    global global_config
    if global_config is None:
        global_config = setup_config(dictionary)
    else:
        global_config.update(config.config_from_dict(dictionary))
    return global_config


def home_yaml_config():
    home = os.path.expanduser("~")
    home_config_path = os.path.join(home, ".powerml/configure_llama.yaml")
    if os.path.exists(home_config_path):
        yaml_config = config.config_from_yaml(home_config_path, read_from_file=True)
    else:
        yaml_config = config.config_from_dict({})
    return yaml_config

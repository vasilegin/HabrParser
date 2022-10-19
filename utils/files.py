import os
import yaml

_configs = {}

ROOT_PATH = os.getcwd()
ASSETS_PATH = os.path.join(ROOT_PATH , "assets")
CONFIG_PATH = os.path.join(ASSETS_PATH , "config")

def read_yaml(filename):
    with open(filename) as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def get_assets(id_: str):
    global _configs
    _config = _configs.get(id_, None)
    if _config is None:
        _configs[id_] = read_yaml(os.path.join(ASSETS_PATH, f'{id_}.yml'))
    return _configs[id_]

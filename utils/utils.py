import yaml


def get_configs(path: str):
    params = yaml.safe_load(open(path, "r", encoding="utf-8"))
    return params
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 CakieJoy

import yaml


def check_in_config(parent_key: str, child_key: str, default_data: str | bool | list[str]):
    with open("./data/config.yaml", "r") as config_file:
        data = yaml.safe_load(config_file)

    if child_key is None:
        if parent_key in data:
            return data.get(parent_key)
        else:
            print(f"Warning: Missing {parent_key} in config.yaml. Using default value: {default_data}", flush=True)
            return default_data
    

    parent = data.get(parent_key, {})

    if child_key in parent:
        return parent.get(child_key)
    else:
        print(f"Warning: Missing {child_key} in config.yaml under {parent_key}. Using default value: {default_data}", flush=True)
        return default_data


def reload_config():
    global PROD_CHECK, ADMIN_LIST

    PROD_CHECK = check_in_config("debug", "IS_PROD", False)
    ADMIN_LIST = check_in_config("admin-list", None, [])


reload_config()
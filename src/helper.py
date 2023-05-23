import sys
import os
from pathlib import Path
from configparser import ConfigParser
import json


class ConfHelper(object):
    conf_file = "./settings.ini"
    record_list: list[(str, str)] = []

    def get_records() -> list[(str, str)]:
        ConfHelper.record_list = []
        if not FileHelper.check_file_exist():
            FileHelper.create_config()
        his = ConfHelper.get_history()
        return [(his["input"], his["output"])]

    def get_history():
        conf = ConfigParser()
        try:
            conf.read(ConfHelper.conf_file)
            his = conf.get("history", "latest")
        except Exception as e:
            default = {
                "input": ".",
                "output": "./output",
            }
            his = default
        return his

    def write_into_file(input, output):
        if FileHelper.check_file_exist():
            FileHelper.create_config()
        conf = ConfigParser()
        conf.read(ConfHelper.conf_file)
        dict1 = {
            "input": input,
            "output": output,
        }
        conf.set("history", "latest", json.dumps(dict1))
        with open(ConfHelper.conf_file, "w", encoding="utf-8") as f:
            conf.write(f)


class FileHelper:
    def create_config():
        # 创建 settings.ini
        conf_file = ConfHelper.conf_file
        os.open(path=conf_file, flags="w", mode=755)
        return

    def check_file_exist() -> bool:
        if not os.path.exists("./settings.ini"):
            print("setting file not exist")
            return False
        else:
            print("setting file exist")
            return True

import sys
import os
from pathlib import Path
from configparser import ConfigParser


class FileHelper:
    def create_config():
        # 创建 settings.ini
        os.open(path="./settings.ini", flags="w", mode=755)
        return

    def check_file_exist() -> bool:
        if not os.path.exists("./settings.ini"):
            print("setting file not exist")
            return False
        else:
            print("setting file exist")
            return True


class ConfHelper(object):
    record_list: list[(str, str)] = []

    def get_records() -> list[str]:
        ConfHelper.record_list = []
        if not FileHelper.check_file_exist():
            FileHelper.create_config()
        return

    def read_conf():
        conf = ConfigParser()
        conf.read("./settings.ini")
        print(conf["default"]["inputDir"])

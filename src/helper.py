import sys
import os
from configparser import ConfigParser


class FileHelper:
    def create_config():
        # 检查 setting
        # 创建 settings.ini
        pwd = os.curdir
        return


class ConfHelper:
    record_list: list[str] = []

    def get_records() -> list[str]:
        return

    def read_conf():
        conf = ConfigParser()
        conf.read("./settings.ini")
        print(conf["default"]["inputDir"])

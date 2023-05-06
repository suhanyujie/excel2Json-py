#!coding=utf-8
import sys
import importlib

importlib.reload(sys)
import os
import xlrd
import json
import os.path
import sys
import shutil


class Convert:
    def getDstDir():
        curPath = os.getcwd()
        dirName = os.path.basename(curPath)
        dstMap = {
            "农场": "farm",
        }
        targetPathPart = dstMap[dirName]
        targetPath = "../../config/" + targetPathPart + "/"
        targetPath = targetPath.replace("/", os.path.sep)
        print("targetPath: ", targetPath)
        # D:\tmp\output\
        return targetPath

    def transDir(self, dir: str) -> str:
        targetPath = dir.replace("/", os.path.sep)
        return targetPath

    # 获取当前程序所在目录
    def getWorkDir():
        frozen = "not"
        if getattr(sys, "frozen", False):
            frozen = "ever so"
            return os.path.dirname(sys.executable)

        return os.path.split(os.path.realpath(__file__))[0]

    def run(self, inputDir: str, outputDir: str):
        workPath = inputDir
        print("fullPath")
        jsonFileTargetDir = self.transDir(outputDir)
        outDir = os.path.join(workPath, "out")
        if os.path.exists(outDir):
            shutil.rmtree(outDir)
        os.mkdir(outDir)
        if input == "":
            workPath = self.getWorkDir()
        for fileName in os.listdir(workPath):
            fullPath = os.path.join(workPath, fileName)
            # print(fullPath)
            fName = os.path.splitext(fullPath)[0]
            extName = os.path.splitext(fullPath)[1]
            if not (extName == ".xlsx" or extName == ".csv"):
                continue
            if fName.find("~") >= 0:
                continue
            workbook = xlrd.open_workbook(fullPath)
            # print("fullPath: ", fullPath)
            # print("sheet num: ", workbook.nsheets)
            for idx in range(0, workbook.nsheets):
                sheet = workbook.sheet_by_index(idx)
                # print("sheet name: ", sheet.name)
                # print("sheet row num: ", sheet.nrows)
                if sheet.nrows < 3:
                    continue
                # colName = sheet.row_values(0)
                colTitle = sheet.row_values(1)
                colType = sheet.row_values(2)
                titleLen = len(colTitle)

                data = []
                for i in range(3, sheet.nrows):
                    row_list = sheet.row_values(i)
                    if row_list[0] == "":
                        continue
                    tmp = {}
                    for j in range(titleLen):
                        if row_list[j] == "yes":
                            row_list[j] = True
                        elif row_list[j] == "no":
                            row_list[j] = False
                        if colType[j] == "int":
                            row_list[j] = int(row_list[j])
                        elif colType[j] == "bool":
                            if row_list[j] == "是" or row_list[j] == "否":
                                row_list[j] = row_list[j] == "是"
                            else:
                                row_list[j] = row_list[j]

                        if isinstance(colTitle[j], str):
                            colTitle[j] = colTitle[j].strip()
                            if colTitle[j] == "":
                                continue
                        if isinstance(row_list[j], str):
                            row_list[j] = row_list[j].strip()
                        if (
                            isinstance(row_list[j], str)
                            and row_list[j].startswith("[")
                            and row_list[j].endswith("]")
                        ):
                            tmp_arr = json.loads(row_list[j])
                            tmp[colTitle[j]] = tmp_arr
                        else:
                            tmp[colTitle[j]] = row_list[j]
                    data.append(tmp)
                if len(data) == 0:
                    continue
                jsonPath = os.path.join(outDir, sheet.name + ".json")
                # print(outDir, sheet.name)
                print(jsonPath)
                with open(jsonPath, "w+") as f:
                    f.write(json.dumps(data))
                shutil.copy(jsonPath, jsonFileTargetDir)
                # 处理完一个 sheet 就退出。只需支持单 sheet 文件
                break

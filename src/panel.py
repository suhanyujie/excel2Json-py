import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QMessageBox,
    QFileDialog,
    QMenuBar,
    QLineEdit,
    QTextBrowser,
)
from PyQt6.QtGui import QIcon, QAction
from pathlib import Path
from convert import Convert
from helper import ConfHelper


class Panel(QWidget):
    inputDir = ""
    outputDir = "output"
    oneHistory = ("", "")

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 480, 320)
        self.setWindowTitle("选择目录")

        self.btn = QPushButton("选择 xlsx 文件目录", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialogInput)
        self.nameLineEdit = QLineEdit(self)
        self.nameLineEdit.move(140, 20)
        self.nameLineEdit.setMinimumWidth(260)

        self.btn1 = QPushButton("选择导出目录", self)
        self.btn1.move(20, 50)
        self.btn1.clicked.connect(self.showDialogOutput)
        self.nameLineEdit1 = QLineEdit(self)
        self.nameLineEdit1.move(140, 50)
        self.nameLineEdit1.setMinimumWidth(200)

        self.tips = QTextBrowser(self)
        self.tips.setMinimumWidth(200)
        self.tips.setMinimumHeight(100)
        self.tips.move(10, 120)
        self.setTips("欢迎使用~")

        self.btn2 = QPushButton("开始转换", self)
        self.btn2.setMinimumWidth(120)
        self.btn2.setMinimumHeight(80)
        self.btn2.move(300, 200)
        self.btn2.clicked.connect(self.startConvert)

    def showDialogInput(self) -> str:
        fname = QFileDialog.getExistingDirectory(directory="./")
        if fname == "":
            fname = "./"
        self.inputDir = fname
        self.nameLineEdit.setText(self.inputDir)
        return fname

    def showDialogOutput(self) -> str:
        fname = QFileDialog.getExistingDirectory(directory="./output")
        if fname == "":
            fname = "./output"
        self.outputDir = fname
        self.nameLineEdit1.setText(self.outputDir)
        return fname

    def startConvert(self):
        try:
            print(self.inputDir)
            print(self.outputDir)
            if self.inputDir == "":
                raise ValueError("请选择要转换的 xlsx 文件目录")
            if self.outputDir == "":
                raise ValueError("请选择转换后输出的目录")
            Convert().run(self.inputDir, self.outputDir)
        except Exception as e:
            self.setTips(e)
        else:
            self.setTips("转换完成~")
            self.oneHistory[0] = self.inputDir
            self.oneHistory[1] = self.outputDir
            # 写入文件
            ConfHelper.write_into_file(self.oneHistory[0], self.oneHistory[1])

    def on_button_clicked(self):
        alert = QMessageBox()
        alert.setText("you clicked...")
        alert.exec()

    def setTips(self, text: str):
        content = "<h3>{text}</h3>".format(text=text)
        self.tips.setText(content)

    def writeIntoFile(self):
        return

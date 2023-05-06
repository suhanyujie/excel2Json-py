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
)
from PyQt6.QtGui import QIcon, QAction
from pathlib import Path
from convert import Convert


class Panel(QWidget):
    inputDir = ""
    outputDir = "output"

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
        self.nameLineEdit.move(160, 20)
        self.nameLineEdit.setMinimumWidth(280)

        self.btn1 = QPushButton("选择导出目录", self)
        self.btn1.move(20, 50)
        self.btn1.clicked.connect(self.showDialogOutput)
        self.nameLineEdit1 = QLineEdit(self)
        self.nameLineEdit1.move(100, 50)
        self.nameLineEdit1.setMinimumWidth(200)

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
        print(self.inputDir)
        print(self.outputDir)
        Convert().run(self.inputDir, self.outputDir)

    def on_button_clicked(self):
        alert = QMessageBox()
        alert.setText("you clicked...")
        alert.exec()

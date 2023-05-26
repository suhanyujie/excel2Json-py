import sys
from PyQt6.QtWidgets import (
    QApplication,
)
from panel import Panel

# from helper import ConfHelper, FileHelper


def main():
    app = QApplication(sys.argv)
    panel = Panel()
    panel.show()
    res = app.exec()
    print(res)
    sys.exit()


if __name__ == "__main__":
    main()

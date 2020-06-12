import sys
import pymysql
pymysql.install_as_MySQLdb()

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication([])
    label = QLabel('Hello World!')
    label.show()
    app.exec_()
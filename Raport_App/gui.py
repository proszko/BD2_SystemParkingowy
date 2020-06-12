import sys
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

if __name__ == "__main__":

    db = MySQLdb.connect("localhost","root","tYPSa5q74XhGDn5g","database_test" )
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print(data)
    db.close()

    app = QApplication([])
    label = QLabel('Hello World!')
    label.show()
    app.exec_()



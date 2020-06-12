import sys
import pymysql
pymysql.install_as_MySQLdb()
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tabWidget = QTabWidget()
    tabWidget.addTab(QTextEdit(), "Hello")
    tabWidget.addTab(QCalendarWidget(), "World")

    tabBar = tabWidget.tabBar()
    menu = QMenu()
    menu.addAction("Open")
    menu.addAction("Close")
    menuButton = QToolButton()
    menuButton.setArrowType(Qt.DownArrow)
    menuButton.setMenu(menu)
    menuButton.setToolButtonStyle(Qt.ToolButtonFollowStyle)
    tabBar.setTabButton(0, QTabBar.RightSide, menuButton)

    tabWidget.show()
    sys.exit(app.exec_())
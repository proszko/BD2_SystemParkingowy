import sys
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("RaportApp")
        self.main_window_init()

    def main_window_init(self):
        self.dateEdit = QDateEdit(QDate.currentDate())
        self.dateEdit.setMaximumDate(QDate.currentDate())
        self.dateEdit.setDisplayFormat("dd.MM.yyyy")

        self.dateEdit2 = QDateEdit(QDate.currentDate())
        self.dateEdit2.setMaximumDate(QDate.currentDate())
        self.dateEdit2.setDisplayFormat("dd.MM.yyyy")

        self.cal1 = CalendarWindow(self.dateEdit.date())
        self.cal2 = CalendarWindow(self.dateEdit2.date())

        self.dateEdit.userDateChanged.connect(self.cal1.calendar.setSelectedDate)
        self.dateEdit2.userDateChanged.connect(self.cal2.calendar.setSelectedDate)

        self.cal1.calendar.clicked.connect(self.dateEdit.setDate)
        self.cal2.calendar.clicked.connect(self.dateEdit2.setDate)

        self.cal1.reset_signal.connect(self.dateEdit.setDate)
        self.cal2.reset_signal.connect(self.dateEdit2.setDate)


        radiobutton = QRadioButton("przychody")
        radiobutton.setChecked(True)
        radiobutton2 = QRadioButton("użycie")

        generateButton = QPushButton("Wygeneruj raport")

        label1 = QLabel("Data rozpoczęcia")
        label2 = QLabel("Data zakończenia")


        hbox = QGridLayout()

        calendarButton1 = QPushButton("")
        calendarButton2 = QPushButton("")

        calendarButton1.setIcon(QIcon("calendar.png"))
        calendarButton2.setIcon(QIcon("calendar.png"))

        calendarButton1.clicked.connect(self.calendar_window1)
        calendarButton2.clicked.connect(self.calendar_window2)

        generateButton.clicked.connect(self.generate_raport)



        hbox.addWidget(label1,0,0)
        hbox.addWidget(self.dateEdit,0,1)
        hbox.addWidget(calendarButton1,0,2)
        hbox.addWidget(label2, 1, 0)
        hbox.addWidget(self.dateEdit2,1,1)
        hbox.addWidget(calendarButton2,1,2)
        hbox.addWidget(radiobutton,2,0)
        hbox.addWidget(radiobutton2,2,1)
        hbox.addWidget(generateButton)


        self.setLayout(hbox)


    def calendar_window1(self):
        self.cal1.initDate = self.dateEdit.date()
        self.cal1.show()

    def calendar_window2(self):
        self.cal2.initDate = self.dateEdit2.date()
        self.cal2.show()

    def generate_raport(self):
        self.raport_table = QTableWidget()
        self.raport_table.show()
        pass



class CalendarWindow(QWidget):
    reset_signal = pyqtSignal(QDate)
    def __init__(self, selected):
        super().__init__()
        self.setWindowTitle("Wybierz datę")
        self.initUI()
        self.initDate = QDate.currentDate()

    def initUI(self):
        self.calendar = QCalendarWidget()
        self.calendar.setMaximumDate(QDate.currentDate())

        buttonOK = QPushButton("OK")
        buttonOK.clicked.connect(self.closeCalendar)


        self.buttonCancel = QPushButton("Anuluj")
        self.buttonCancel.clicked.connect(self.emitResetSignal)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.calendar)
        hbox.addWidget(buttonOK)
        hbox.addWidget(self.buttonCancel)

        self.setLayout(hbox)

    def emitResetSignal(self):
        self.reset_signal.emit(self.initDate)
        self.hide()

    def closeCalendar(self):
        self.hide()





if __name__ == "__main__":

#    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test" )
#    cursor = db.cursor()
#    cursor.execute("SELECT VERSION()")
#    data = cursor.fetchone()
#    print(data)
#    db.close()

    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



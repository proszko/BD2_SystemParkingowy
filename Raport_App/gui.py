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


        self.checkbox = QCheckBox("przychody")
        self.checkbox2 = QCheckBox("użycie")
        self.checkbox3 = QCheckBox("użytkownicy")

        generateButton = QPushButton("Wygeneruj raport")

        label1 = QLabel("Data rozpoczęcia")
        label2 = QLabel("Data zakończenia")
        label3 = QLabel("Strefa:")


        hbox = QGridLayout()

        calendarButton1 = QPushButton("")
        calendarButton2 = QPushButton("")

        calendarButton1.setIcon(QIcon("calendar.png"))
        calendarButton2.setIcon(QIcon("calendar.png"))

        calendarButton1.clicked.connect(self.calendar_window1)
        calendarButton2.clicked.connect(self.calendar_window2)

        generateButton.clicked.connect(self.generateRaports)

        self.comboBox = QComboBox(self)
        strefy_list = getAllStrefy()
        for name in strefy_list:
            self.comboBox.addItems(name)

        hbox.addWidget(label1,0,0)
        hbox.addWidget(self.dateEdit,0,1)
        hbox.addWidget(calendarButton1,0,2)
        hbox.addWidget(label2, 1, 0)
        hbox.addWidget(self.dateEdit2,1,1)
        hbox.addWidget(calendarButton2,1,2)
        hbox.addWidget(self.checkbox,2,0)
        hbox.addWidget(self.checkbox2,2,1)
        hbox.addWidget(self.checkbox3, 2, 2)
        hbox.addWidget(generateButton, 4, 1)
        hbox.addWidget(label3, 3, 0)
        hbox.addWidget(self.comboBox, 3, 1)

        self.setLayout(hbox)


    def calendar_window1(self):
        self.cal1.initDate = self.dateEdit.date()
        self.cal1.show()

    def calendar_window2(self):
        self.cal2.initDate = self.dateEdit2.date()
        self.cal2.show()

    def generateRaports(self):
        if self.dateEdit.dateTime() > self.dateEdit2.dateTime():
            self.alert_widget = QMessageBox()
            self.alert_widget.setIcon(QMessageBox.Warning)
            self.alert_widget.setText("Nieprawidłowy zakres dat")
            self.alert_widget.show()
            return
        if (self.checkbox.isChecked()):
            self.generateUsageRaport()
        if (self.checkbox2.isChecked()):
            self.generateProfitRaport()
        if (self.checkbox3.isChecked()):
            self.generateUserRaport()

    def generateUsageRaport(self):

        

        self.raport_usage = QTableWidget()
        self.raport_usage.setRowCount(30)
        self.raport_usage.setColumnCount(7)


        strefa = self.comboBox.currentText()
        startDate = self.dateEdit.dateTime()
        endDate = self.dateEdit2.dateTime()

        
        strefy_name = window.comboBox.currentText()
        self.raport_usage.setItem(0, 0, QTableWidgetItem(strefy_name))
        self.raport_usage.setItem(0, 1, QTableWidgetItem(startDate.toString('dd.MM.yyyy')))
        self.raport_usage.setItem(0, 2, QTableWidgetItem(endDate.toString('dd.MM.yyyy')))
        
        startDate = startDate.toString('yyyy-MM-dd hh:mm:ss')
        endDate = endDate.addDays(1).toString('yyyy-MM-dd hh:mm:ss')


        self.raport_usage.setItem(2, 0, QTableWidgetItem("Ogółem pobytów:"))
        data = getPobytNumbers(startDate, endDate, strefa)

        if data is not None:
            self.raport_usage.setItem(2, 1, QTableWidgetItem(str(data[2])))
        else:
            self.raport_usage.setItem(2, 1, QTableWidgetItem('0'))

        data = getPobytNumbersByParking(startDate, endDate, strefa)
        self.raport_usage.setItem(3, 0, QTableWidgetItem("z parkowaniem:"))
        self.raport_usage.setItem(4, 0, QTableWidgetItem("bez parkowania:"))

        if len(data) == 0:
            self.raport_usage.setItem(3, 1, QTableWidgetItem('0'))
            self.raport_usage.setItem(4, 1, QTableWidgetItem('0'))
        elif len(data) == 2:
            self.raport_usage.setItem(3, 1, QTableWidgetItem(str(data[0][3])))
            self.raport_usage.setItem(4, 1, QTableWidgetItem(str(data[1][3])))
        elif len(data) == 1:
            if data[0][2] == 'z_parkowaniem':
                self.raport_usage.setItem(3, 1, QTableWidgetItem(str(data[0][3])))
                self.raport_usage.setItem(4, 1, QTableWidgetItem('0'))
            else:
                self.raport_usage.setItem(3, 1, QTableWidgetItem('0'))
                self.raport_usage.setItem(4, 1, QTableWidgetItem(str(data[0][3])))




        pojazdy_list = getAllTypyPojazdow()
        self.raport_usage.setItem(6, 0, QTableWidgetItem("Typ pojazdu"))
        self.raport_usage.setItem(6, 1, QTableWidgetItem("Ilość pobytów"))
        self.raport_usage.setItem(6, 2, QTableWidgetItem("Ilość parkowań"))
        self.raport_usage.setItem(6, 3, QTableWidgetItem("Użycie parkingu [%]"))


        i = 7
        for pojazd in pojazdy_list:
            self.raport_usage.setItem(i, 0, QTableWidgetItem(pojazd[0]))
            self.raport_usage.setItem(i, 1, QTableWidgetItem('0'))
            self.raport_usage.setItem(i, 2, QTableWidgetItem('0'))
            self.raport_usage.setItem(i, 3, QTableWidgetItem('0'))
            i += 1

        data = getPobytNumbersByStrefaAndTypPojazdu(startDate, endDate, strefa)
        for el in data:
            self.raport_usage.setItem(6 + el[2], 1, QTableWidgetItem(str(el[4])))

        data = getParkingUsage(startDate, endDate, strefa)
        for el in data:
            self.raport_usage.setItem(6 + el[2], 2, QTableWidgetItem(str(el[4])))
            self.raport_usage.setItem(6 + el[2], 3, QTableWidgetItem(str(el[5])))

        
        i+=2
        self.raport_usage.setItem(i, 0, QTableWidgetItem("Nazwa bramki wjazdowej"))
        self.raport_usage.setItem(i, 1, QTableWidgetItem("Ilość użyć"))
        self.raport_usage.setItem(i, 3, QTableWidgetItem("Nazwa bramki wyjazdowej"))
        self.raport_usage.setItem(i, 4, QTableWidgetItem("Ilość użyć"))
        i+=1
        data = getWjazdoweBramkiUsage(startDate, endDate, strefa)
        
        i_ref1 = i
        i_ref2 = i
        for j in range(len(data)):
            self.raport_usage.setItem(i_ref1, 0, QTableWidgetItem(data[j][2]))
            self.raport_usage.setItem(i_ref1, 1, QTableWidgetItem(str(data[j][4])))
            i_ref1+=1

        i_ref2 = i
        data = getWyjazdoweBramkiUsage(startDate, endDate, strefa)
        for j in range(len(data)):
            self.raport_usage.setItem(i_ref2, 3, QTableWidgetItem(data[j][2]))
            self.raport_usage.setItem(i_ref2, 4, QTableWidgetItem(str(data[j][4])))
            i_ref2+=1

        self.raport_usage.setGeometry(50,50,700,800)
        self.raport_usage.show()

        

    def generateProfitRaport(self):
        self.raport_profit = QTableWidget()
        self.raport_profit.setRowCount(30)
        self.raport_profit.setColumnCount(7)


        strefa = self.comboBox.currentText()
        startDate = self.dateEdit.dateTime()
        endDate = self.dateEdit2.dateTime()


        strefy_name = window.comboBox.currentText()
        self.raport_profit.setItem(0, 0, QTableWidgetItem(strefy_name))
        self.raport_profit.setItem(0, 1, QTableWidgetItem(startDate.toString('dd.MM.yyyy')))
        self.raport_profit.setItem(0, 2, QTableWidgetItem(endDate.toString('dd.MM.yyyy')))

        startDate = startDate.toString('yyyy-MM-dd hh:mm:ss')
        endDate = endDate.addDays(1).toString('yyyy-MM-dd hh:mm:ss')


        self.raport_profit.setItem(2, 1, QTableWidgetItem("Przychód"))
        self.raport_profit.setItem(2, 2, QTableWidgetItem("Przychód z ulgami"))

        self.raport_profit.setItem(3, 0, QTableWidgetItem("Ogólny:"))
        self.raport_profit.setItem(4, 0, QTableWidgetItem("Ta strefa:"))
        self.raport_profit.setItem(5, 0, QTableWidgetItem("Udział [%]:"))

        data = getProfit(startDate, endDate)


        if data[0] is not None:
            profit = data[0]
            self.raport_profit.setItem(3, 1, QTableWidgetItem(str(profit)))
        else:
            profit = 0.0
            self.raport_profit.setItem(3, 1, QTableWidgetItem('0'))


        data = round(getReducedProfit(startDate, endDate),2)
        reducedProfit = data
        self.raport_profit.setItem(3, 2, QTableWidgetItem(str(data)))


        pojazdy_list = getAllTypyPojazdow()



        self.raport_profit.setItem(7, 0, QTableWidgetItem("Typ pojazdu"))
        self.raport_profit.setItem(7, 1, QTableWidgetItem("Przychód"))
        self.raport_profit.setItem(7, 2, QTableWidgetItem("Przychód z ulgami"))


        i = 8
        for pojazd in pojazdy_list:
            self.raport_profit.setItem(i, 0, QTableWidgetItem(pojazd[0]))
            self.raport_profit.setItem(i, 1, QTableWidgetItem('0'))
            self.raport_profit.setItem(i, 2, QTableWidgetItem('0'))

            i += 1

        data = getProfitByStrefaAndTypPojazdu(startDate, endDate, strefa)
        sum = 0
        for el in data:
            self.raport_profit.setItem(7+el[2], 1, QTableWidgetItem(str(el[4])))
            sum += el[4]
        sum = round(sum, 2)
        self.raport_profit.setItem(4, 1, QTableWidgetItem(str(sum)))
        if sum != 0:
            self.raport_profit.setItem(5, 1, QTableWidgetItem(str(round(100*sum/profit,2))))
        else:
            self.raport_profit.setItem(5, 1, QTableWidgetItem('0'))


        data = getReducedProfitByStrefaAndTypPojazdu(startDate, endDate, strefa)
        print(data)
        sum = 0
        for i in range(len(data)):
            data[i] = round (data[i], 2)
            sum+=data[i]
            self.raport_profit.setItem(8 + i, 2, QTableWidgetItem(str(data[i])))


        sum = round(sum, 2)
        self.raport_profit.setItem(4, 2, QTableWidgetItem(str(sum)))
        if sum != 0:
            self.raport_profit.setItem(5, 2, QTableWidgetItem(str(round(100 * sum / reducedProfit, 2))))
        else:
            self.raport_profit.setItem(5, 2, QTableWidgetItem('0'))



        self.raport_profit.setGeometry(50,50,600,800)
        self.raport_profit.show()
        
    def generateUserRaport(self):


        self.raport_user = QTableWidget()
        self.raport_user.setRowCount(30)
        self.raport_user.setColumnCount(7)

        startDate = self.dateEdit.dateTime()
        endDate = self.dateEdit2.dateTime()

        self.raport_user.setItem(0, 0, QTableWidgetItem("Aktywność użytkowników"))
        self.raport_user.setItem(0, 1, QTableWidgetItem(startDate.toString('dd.MM.yyyy')))
        self.raport_user.setItem(0, 2, QTableWidgetItem(endDate.toString('dd.MM.yyyy')))

        startDate = startDate.toString('yyyy-MM-dd hh:mm:ss')
        endDate = endDate.addDays(1).toString('yyyy-MM-dd hh:mm:ss')

        self.raport_user.setItem(2, 0, QTableWidgetItem("id konta"))
        self.raport_user.setItem(2, 1, QTableWidgetItem("imię"))
        self.raport_user.setItem(2, 2, QTableWidgetItem("nazwisko"))
        self.raport_user.setItem(2, 3, QTableWidgetItem("ilość pobytów"))
        self.raport_user.setItem(2, 4, QTableWidgetItem("łączna należność"))

        i = 3

        data = getUserStats(startDate, endDate)
        print(data)
        self.raport_user.setRowCount(len(data)+3)
        for user in data:
            self.raport_user.setItem(i, 0, QTableWidgetItem(str(user[0])))
            self.raport_user.setItem(i, 1, QTableWidgetItem(str(user[1])))
            self.raport_user.setItem(i, 2, QTableWidgetItem(str(user[2])))
            self.raport_user.setItem(i, 3, QTableWidgetItem(str(user[4])))
            self.raport_user.setItem(i, 4, QTableWidgetItem(str(user[3])))
            i+=1

        self.raport_user.setGeometry(50,50,600,800)
        self.raport_user.show()


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




def getAllStrefy():
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test" )
    cursor = db.cursor()
    sql_strefynames = "SELECT nazwa FROM strefy ORDER BY nazwa"
    cursor.execute(sql_strefynames)
    data = cursor.fetchall()
    db.close()
    return data


def getAllTypyPojazdow():
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test")
    cursor = db.cursor()
    sql_pojazdynames = "SELECT nazwa from typy_pojazdów ORDER BY nazwa"
    cursor.execute(sql_pojazdynames)
    data = cursor.fetchall()
    db.close()
    return data



def getPobytNumbers(startTime, endTime, strefa):
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test")
    cursor = db.cursor()

    # Pobranie liczby pobytów w każdej strefie
    sql = "SELECT bramki.strefy_id, strefy.nazwa, COUNT(*) FROM pobyty\
    INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
    INNER JOIN strefy ON bramki.strefy_id = strefy.id\
    WHERE godzina_zakonczenia BETWEEN %s AND %s\
    AND strefy.nazwa = %s \
    GROUP BY bramki.strefy_id\
    ORDER BY bramki.strefy_id"

    cursor.execute(sql, [startTime, endTime, strefa])
    data = cursor.fetchone()
    db.close()
    return data


def getPobytNumbersByParking(startTime, endTime, strefa):
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test")
    cursor = db.cursor()

    # Podział wszystkich pobytów, grupowanie po pobytach z parkowaniem i bez
    sql = "SELECT bramki.strefy_id, strefy.nazwa, pobyty.selektor, COUNT(*) FROM pobyty\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        WHERE godzina_zakonczenia BETWEEN %s AND %s\
        AND strefy.nazwa = %s \
        GROUP BY bramki.strefy_id, pobyty.selektor\
        ORDER BY bramki.strefy_id, pobyty.selektor"

    cursor.execute(sql, [startTime, endTime, strefa])
    data = cursor.fetchall()
    db.close()
    return data


def getPobytNumbersByStrefaAndTypPojazdu(startTime, endTime, strefa):
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test")
    cursor = db.cursor()

    # Podział wszystkich pobytów grupowanie po strefie i typie pojazdu
    sql = "SELECT bramki.strefy_id, strefy.nazwa, typy_pojazdów.id,  \
        typy_pojazdów.nazwa, COUNT(*), SEC_TO_TIME(FLOOR(AVG(TIMESTAMPDIFF(SECOND, godzina_rozpoczecia, godzina_zakonczenia)))) \
        FROM pobyty\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        INNER JOIN pojazdy ON pobyty.pojazdy_rejestracja = pojazdy.rejestracja\
        INNER JOIN typy_pojazdów ON pojazdy.typy_pojazdów_id = typy_pojazdów.id\
        WHERE godzina_zakonczenia BETWEEN %s AND %s\
        AND strefy.nazwa = %s \
        GROUP BY bramki.strefy_id, typy_pojazdów.id\
        ORDER BY bramki.strefy_id, typy_pojazdów.id"\

    cursor.execute(sql, [startTime, endTime, strefa])
    data = cursor.fetchall()
    db.close()
    return data

def getPobytNumbersByStrefaAndTypPojazdu(startTime, endTime, strefa):
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test")
    cursor = db.cursor()

    # Podział wszystkich pobytów grupowanie po strefie i typie pojazdu
    sql = "SELECT bramki.strefy_id, strefy.nazwa, typy_pojazdów.id,  \
        typy_pojazdów.nazwa, COUNT(*), SEC_TO_TIME(FLOOR(AVG(TIMESTAMPDIFF(SECOND, godzina_rozpoczecia, godzina_zakonczenia)))) \
        FROM pobyty\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        INNER JOIN pojazdy ON pobyty.pojazdy_rejestracja = pojazdy.rejestracja\
        INNER JOIN typy_pojazdów ON pojazdy.typy_pojazdów_id = typy_pojazdów.id\
        WHERE godzina_zakonczenia BETWEEN %s AND %s\
        AND strefy.nazwa = %s \
        GROUP BY bramki.strefy_id, typy_pojazdów.id\
        ORDER BY bramki.strefy_id, typy_pojazdów.id"\

    cursor.execute(sql, [startTime, endTime, strefa])
    data = cursor.fetchall()
    db.close()
    return data

def getParkingUsage(startTime, endTime, strefa):
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test")
    cursor = db.cursor()

    # Wyliczenie średniego zużycia parkingów
    sql = "SELECT bramki.strefy_id, strefy.nazwa, pojazdy.typy_pojazdów_id, typy_pojazdów.nazwa, COUNT(*),\
        100 * SEC_TO_TIME(SUM(TIMESTAMPDIFF(SECOND, godzina_rozpoczecia, godzina_zakonczenia)))/(pojemności.miejsca * TIMESTAMPDIFF(SECOND, %s, %s))\
        FROM pobyty\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        INNER JOIN pojazdy ON pobyty.pojazdy_rejestracja = pojazdy.rejestracja\
        INNER JOIN typy_pojazdów ON pojazdy.typy_pojazdów_id = typy_pojazdów.id\
        INNER JOIN pojemności ON pojemności.typy_pojazdów_id = pojazdy.typy_pojazdów_id AND pojemności.strefy_id = bramki.strefy_id\
        WHERE godzina_zakonczenia BETWEEN %s AND %s\
        AND strefy.nazwa = %s \
        AND pobyty.selektor = 'z_parkowaniem'\
        GROUP BY bramki.strefy_id, typy_pojazdów.id\
        ORDER BY bramki.strefy_id, typy_pojazdów.id;"

    cursor.execute(sql, [startTime, endTime, startTime, endTime, strefa ])

    data = cursor.fetchall()
    db.close()
    return data


def getWjazdoweBramkiUsage(startTime, endTime, strefa):
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test")
    cursor = db.cursor()

    # Wyliczenie użycia bramek wjazdowych
    sql = "SELECT bramki.strefy_id, strefy.nazwa, bramki.nazwa, bramki.selektor, COUNT(*) FROM pobyty\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        WHERE godzina_zakonczenia BETWEEN %s AND %s\
        AND strefy.nazwa = %s \
        GROUP BY bramki.strefy_id, bramki.nazwa, bramki.selektor\
        ORDER BY bramki.strefy_id, COUNT(*) DESC";

    cursor.execute(sql, [startTime, endTime, strefa])
    data = cursor.fetchall()
    db.close()
    return data


def getWyjazdoweBramkiUsage(startTime, endTime, strefa):
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test")
    cursor = db.cursor()

    # Wyliczenie użycia bramek wyjazdowych
    sql = "SELECT bramki.strefy_id, strefy.nazwa, bramki.nazwa, bramki.selektor, COUNT(*) FROM pobyty\
        INNER JOIN bramki ON pobyty.wyjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        WHERE godzina_zakonczenia BETWEEN %s AND %s\
        AND strefy.nazwa = %s \
        GROUP BY bramki.strefy_id, bramki.nazwa, bramki.selektor\
        ORDER BY bramki.strefy_id, COUNT(*) DESC";

    cursor.execute(sql, [startTime, endTime, strefa])
    data = cursor.fetchall()
    db.close()
    return data

def getProfit(startTime, endTime):
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test")
    cursor = db.cursor()

    # Niepotrącony przychód
    sql = "SELECT ROUND(SUM(należność),2), COUNT(*) FROM pobyty\
        WHERE godzina_zakonczenia BETWEEN %s AND %s"

    cursor.execute(sql, [startTime, endTime])
    data = cursor.fetchone()
    db.close()
    return data

def getProfitByStrefaAndTypPojazdu(startTime, endTime, strefa):
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test")
    cursor = db.cursor()

    # Niepotrącony przychód z podziałem na strefy i typy pojazdów
    sql = "SELECT bramki.strefy_id, strefy.nazwa, pojazdy.typy_pojazdów_id, typy_pojazdów.nazwa, ROUND(SUM(należność),2) \
        FROM pobyty\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        INNER JOIN pojazdy ON pobyty.pojazdy_rejestracja = pojazdy.rejestracja\
        INNER JOIN typy_pojazdów ON pojazdy.typy_pojazdów_id = typy_pojazdów.id\
        WHERE godzina_zakonczenia BETWEEN %s AND %s\
        AND strefy.nazwa = %s \
        GROUP BY bramki.strefy_id, pojazdy.typy_pojazdów_id\
        ORDER BY bramki.strefy_id, pojazdy.typy_pojazdów_id"

    cursor.execute(sql, [startTime, endTime, strefa])
    data = cursor.fetchall()
    db.close()
    return data

def getReducedProfit(startTime, endTime):
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test")
    cursor = db.cursor()

    

    # Potrącony przychód: brak konta
    sql1 = "SELECT ROUND(SUM(należność),2), COUNT(*)\
        FROM pobyty\
        WHERE godzina_zakonczenia BETWEEN %s AND %s\
        AND pobyty.konta_id IS NULL;"

    # Potrącony przychód: konto, brak ulgi
    sql2 = "SELECT ROUND(SUM(należność),2), COUNT(*)\
        FROM pobyty\
        INNER JOIN konta ON pobyty.konta_id = konta.id\
        WHERE godzina_zakonczenia BETWEEN %s AND %s\
        AND pobyty.konta_id IS NOT NULL\
        AND konta.ulgi_id IS NULL;"

    # Potrącony przychód: konto, ulga
    sql3 = "SELECT ROUND(SUM(należność)*(1 - 0.01*ulgi.zniżka) ,2), COUNT(*)\
        FROM pobyty\
        INNER JOIN konta ON pobyty.konta_id = konta.id\
        INNER JOIN ulgi on konta.ulgi_id = ulgi.id\
        WHERE godzina_zakonczenia BETWEEN %s AND %s\
        AND pobyty.konta_id IS NOT NULL\
        AND konta.ulgi_id IS NOT NULL;"

    


    cursor.execute(sql1, [startTime, endTime])
    data1 = cursor.fetchone()
    cursor.execute(sql2, [startTime, endTime])
    data2 = cursor.fetchone()
    cursor.execute(sql3, [startTime, endTime])
    data3 = cursor.fetchone()
    db.close()

    
    result = 0
    if data1[0] is not None:
        result += data1[0]
    if data2[0] is not None:
        result += data2[0]
    if data3[0] is not None:
        result += data3[0]

    

    return result


def getReducedProfitByStrefaAndTypPojazdu(startTime, endTime, strefa):
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test")
    cursor = db.cursor()

    # j.w., tylko z podziałem na typy pojazdow i strefy
    sql1 = "SELECT bramki.strefy_id, strefy.nazwa, pojazdy.typy_pojazdów_id, typy_pojazdów.nazwa, \
        ROUND(SUM(należność),2), COUNT(*) \
        FROM pobyty\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        INNER JOIN pojazdy ON pobyty.pojazdy_rejestracja = pojazdy.rejestracja\
        INNER JOIN typy_pojazdów ON pojazdy.typy_pojazdów_id = typy_pojazdów.id\
        WHERE godzina_zakonczenia BETWEEN %s AND %s\
        AND strefy.nazwa = %s \
        AND pobyty.konta_id IS NULL\
        GROUP BY bramki.strefy_id, pojazdy.typy_pojazdów_id\
        ORDER BY bramki.strefy_id, pojazdy.typy_pojazdów_id;"

    sql2 = "SELECT bramki.strefy_id, strefy.nazwa, pojazdy.typy_pojazdów_id, typy_pojazdów.nazwa, \
        ROUND(SUM(należność),2), COUNT(*) \
        FROM pobyty\
        INNER JOIN konta ON pobyty.konta_id = konta.id\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        INNER JOIN pojazdy ON pobyty.pojazdy_rejestracja = pojazdy.rejestracja\
        INNER JOIN typy_pojazdów ON pojazdy.typy_pojazdów_id = typy_pojazdów.id\
        WHERE godzina_zakonczenia BETWEEN %s AND %s\
        AND strefy.nazwa = %s \
        AND pobyty.konta_id IS NOT NULL\
        AND konta.ulgi_id IS NULL\
        GROUP BY bramki.strefy_id, pojazdy.typy_pojazdów_id\
        ORDER BY bramki.strefy_id, pojazdy.typy_pojazdów_id;"

    sql3 = "SELECT bramki.strefy_id, strefy.nazwa, pojazdy.typy_pojazdów_id, typy_pojazdów.nazwa, \
        ROUND(SUM(należność)*(1 - 0.01*ulgi.zniżka) ,2), COUNT(*)\
        FROM pobyty\
        INNER JOIN konta ON pobyty.konta_id = konta.id\
        INNER JOIN ulgi on konta.ulgi_id = ulgi.id\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        INNER JOIN pojazdy ON pobyty.pojazdy_rejestracja = pojazdy.rejestracja\
        INNER JOIN typy_pojazdów ON pojazdy.typy_pojazdów_id = typy_pojazdów.id\
        WHERE godzina_zakonczenia BETWEEN %s AND %s\
        AND strefy.nazwa = %s \
        AND pobyty.konta_id IS NOT NULL\
        AND konta.ulgi_id IS NOT NULL\
        GROUP BY bramki.strefy_id, pojazdy.typy_pojazdów_id\
        ORDER BY bramki.strefy_id, pojazdy.typy_pojazdów_id;"

    cursor.execute(sql1, [startTime, endTime, strefa])
    data1 = cursor.fetchall()
    cursor.execute(sql2, [startTime, endTime, strefa])
    data2 = cursor.fetchall()
    cursor.execute(sql3, [startTime, endTime, strefa])
    data3 = cursor.fetchall()

    print(data1)
    strefy = getAllTypyPojazdow()
    new_dict = []


    for strefa in strefy:
        new_dict.append(0)


    for el in data1:
        new_dict[el[2]-1] += el[4]
    for el in data2:
        new_dict[el[2]-1] += el[4]
    for el in data3:
        new_dict[el[2]-1] += el[4]

    db.close()
    return new_dict

def getUserStats(startTime, endTime):
    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test")
    cursor = db.cursor()

    # Raport o użytkownikach
    sql = "SELECT pobyty.konta_id, konta.imię, konta.nazwisko,  \
            ROUND(SUM(należność) * (1 - 0.01* ulgi.zniżka),2), COUNT(*) from pobyty \
            INNER JOIN konta ON pobyty.konta_id = konta.id \
            INNER JOIN ulgi ON konta.ulgi_id = ulgi.id \
            WHERE pobyty.godzina_zakonczenia BETWEEN %s AND %s\
            GROUP BY pobyty.konta_id \
            ORDER BY pobyty.konta_id"

    cursor.execute(sql, [startTime, endTime])
    data = cursor.fetchall()
    db.close()
    return data



if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



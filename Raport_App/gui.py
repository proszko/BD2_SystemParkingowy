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

    db = MySQLdb.connect("localhost", "root", "tYPSa5q74XhGDn5g", "database_test" )
    cursor = db.cursor()

    # Pobranie liczby pobytów w każdej strefie
    sql0 = "SELECT bramki.strefy_id, strefy.nazwa, COUNT(*) FROM pobyty\
    INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
    INNER JOIN strefy ON bramki.strefy_id = strefy.id\
    WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'\
    GROUP BY bramki.strefy_id\
    ORDER BY bramki.strefy_id"

    cursor.execute(sql0)
    data = cursor.fetchall()
    print(data)

    # Podział wszystkich pobytów, grupowanie po pobytach z parkowaniem i bez
    sql1 = "SELECT bramki.strefy_id, strefy.nazwa, pobyty.selektor, COUNT(*) FROM pobyty\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'\
        GROUP BY bramki.strefy_id, pobyty.selektor\
        ORDER BY bramki.strefy_id, pobyty.selektor"

    cursor.execute(sql1)
    data = cursor.fetchall()
    print(data)

    # Podział wszystkich pobytów grupowanie po strefie i typie pojazdu
    sql2 = "SELECT bramki.strefy_id, strefy.nazwa, typy_pojazdów.id,  \
        typy_pojazdów.nazwa, COUNT(*), SEC_TO_TIME(FLOOR(AVG(TIMESTAMPDIFF(SECOND, godzina_rozpoczecia, godzina_zakonczenia)))) \
        FROM pobyty\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        INNER JOIN pojazdy ON pobyty.pojazdy_rejestracja = pojazdy.rejestracja\
        INNER JOIN typy_pojazdów ON pojazdy.typy_pojazdów_id = typy_pojazdów.id\
        WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'\
        GROUP BY bramki.strefy_id, typy_pojazdów.id\
        ORDER BY bramki.strefy_id, typy_pojazdów.id"\

    # Wyliczenie średniego zużycia parkingów
    sql3 = "SELECT bramki.strefy_id, strefy.nazwa, pojazdy.typy_pojazdów_id, typy_pojazdów.nazwa, COUNT(*),\
        100 * SEC_TO_TIME(SUM(TIMESTAMPDIFF(SECOND, godzina_rozpoczecia, godzina_zakonczenia)))/(pojemności.miejsca * TIMESTAMPDIFF(SECOND, '2020-01-01 10:10:10', '2020-03-05 10:10:10'))\
        FROM pobyty\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        INNER JOIN pojazdy ON pobyty.pojazdy_rejestracja = pojazdy.rejestracja\
        INNER JOIN typy_pojazdów ON pojazdy.typy_pojazdów_id = typy_pojazdów.id\
        INNER JOIN pojemności ON pojemności.typy_pojazdów_id = pojazdy.typy_pojazdów_id AND pojemności.strefy_id = bramki.strefy_id\
        WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'\
        AND pobyty.selektor = 'z_parkowaniem'\
        GROUP BY bramki.strefy_id, typy_pojazdów.id\
        ORDER BY bramki.strefy_id, typy_pojazdów.id"


    # Wyliczenie użycia bramek wjazdowych
    sql4 = "SELECT bramki.strefy_id, strefy.nazwa, bramki.nazwa, bramki.selektor, COUNT(*) FROM pobyty\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'\
        GROUP BY bramki.strefy_id, bramki.nazwa, bramki.selektor\
        ORDER BY bramki.strefy_id, COUNT(*) DESC";


    # Wyliczenie użycia bramek wyjazdowych
    sql5 = "SELECT bramki.strefy_id, strefy.nazwa, bramki.nazwa, bramki.selektor, COUNT(*) FROM pobyty\
        INNER JOIN bramki ON pobyty.wyjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'\
        GROUP BY bramki.strefy_id, bramki.nazwa, bramki.selektor\
        ORDER BY bramki.strefy_id, COUNT(*) DESC";


    # Niepotrącony przychód
    sql6 = "SELECT ROUND(SUM(należność),2), COUNT(*) FROM pobyty\
        WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'"

    # Niepotrącony przychód z podziałem na strefy i typy pojazdów
    sql7 = "SELECT bramki.strefy_id, strefy.nazwa, pojazdy.typy_pojazdów_id, typy_pojazdów.nazwa, ROUND(SUM(należność),2) \
        FROM pobyty\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        INNER JOIN pojazdy ON pobyty.pojazdy_rejestracja = pojazdy.rejestracja\
        INNER JOIN typy_pojazdów ON pojazdy.typy_pojazdów_id = typy_pojazdów.id\
        WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'\
        GROUP BY bramki.strefy_id, pojazdy.typy_pojazdów_id\
        ORDER BY bramki.strefy_id, pojazdy.typy_pojazdów_id"

    # Potrącony przychód: brak konta
    sql8a = "SELECT ROUND(SUM(należność),2), COUNT(*)\
        FROM pobyty\
        WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'\
        AND pobyty.konta_id IS NULL;"

    # Potrącony przychód: konto, brak ulgi
    sql8b = "SELECT ROUND(SUM(należność),2), COUNT(*)\
        FROM pobyty\
        INNER JOIN konta ON pobyty.konta_id = konta.id\
        WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'\
        AND pobyty.konta_id IS NOT NULL\
        AND konta.ulgi_id IS NULL;"

    # Potrącony przychód: konto, ulga
    sql8c = "SELECT ROUND(SUM(należność)*(1 - 0.01*ulgi.zniżka) ,2), COUNT(*)\
        FROM pobyty\
        INNER JOIN konta ON pobyty.konta_id = konta.id\
        INNER JOIN ulgi on konta.ulgi_id = ulgi.id\
        WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'\
        AND pobyty.konta_id IS NOT NULL\
        AND konta.ulgi_id IS NOT NULL;"

    # j.w., tylko z podziałem na typy pojazdow i strefy
    sql9a = "SELECT bramki.strefy_id, strefy.nazwa, pojazdy.typy_pojazdów_id, typy_pojazdów.nazwa," \
        "ROUND(SUM(należność),2), COUNT(*), \
        FROM pobyty\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        INNER JOIN pojazdy ON pobyty.pojazdy_rejestracja = pojazdy.rejestracja\
        INNER JOIN typy_pojazdów ON pojazdy.typy_pojazdów_id = typy_pojazdów.id\
        WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'\
        AND pobyty.konta_id IS NULL\
        GROUP BY bramki.strefy_id, pojazdy.typy_pojazdów_id\
        ORDER BY bramki.strefy_id, pojazdy.typy_pojazdów_id;"

    sql9b = "SELECT bramki.strefy_id, strefy.nazwa, pojazdy.typy_pojazdów_id, typy_pojazdów.nazwa," \
        "ROUND(SUM(należność),2), COUNT(*), \
        FROM pobyty\
        INNER JOIN konta ON pobyty.konta_id = konta.id\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        INNER JOIN pojazdy ON pobyty.pojazdy_rejestracja = pojazdy.rejestracja\
        INNER JOIN typy_pojazdów ON pojazdy.typy_pojazdów_id = typy_pojazdów.id\
        WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'\
        AND pobyty.konta_id IS NOT NULL\
        AND konta.ulgi_id IS NULL\
        GROUP BY bramki.strefy_id, pojazdy.typy_pojazdów_id\
        ORDER BY bramki.strefy_id, pojazdy.typy_pojazdów_id;"

    sql9c = "SELECT bramki.strefy_id, strefy.nazwa, pojazdy.typy_pojazdów_id, typy_pojazdów.nazwa, \
        ROUND(SUM(należność)*(1 - 0.01*ulgi.zniżka) ,2), COUNT(*)\
        FROM pobyty\
        INNER JOIN konta ON pobyty.konta_id = konta.id\
        INNER JOIN ulgi on konta.ulgi_id = ulgi.id\
        INNER JOIN bramki ON pobyty.wjazdowe_bramki_id = bramki.id\
        INNER JOIN strefy ON bramki.strefy_id = strefy.id\
        INNER JOIN pojazdy ON pobyty.pojazdy_rejestracja = pojazdy.rejestracja\
        INNER JOIN typy_pojazdów ON pojazdy.typy_pojazdów_id = typy_pojazdów.id\
        WHERE godzina_zakonczenia BETWEEN '2020-01-01 10:10:10' AND '2020-03-05 10:10:10'\
        AND pobyty.konta_id IS NOT NULL\
        AND konta.ulgi_id IS NOT NULL\
        GROUP BY bramki.strefy_id, pojazdy.typy_pojazdów_id\
        ORDER BY bramki.strefy_id, pojazdy.typy_pojazdów_id;"


    cursor.execute(sql3)
    data = cursor.fetchall()
    print(data)

    db.close()

#    app = QApplication([])
#    window = MainWindow()
#    window.show()
#    sys.exit(app.exec_())



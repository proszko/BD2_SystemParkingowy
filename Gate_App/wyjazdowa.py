import sys
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

ID_NUMBER = 1


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bramka wyjazdowa")
        self.center()
        self.main_window_init()

    def main_window_init(self):

        self.setFont(QFont('SanSerif', 14))
        button1 = QPushButton("Zakończ pobyt")
        button2 = QPushButton("Sprawdź stan konta")
        button3 = QPushButton("Doładuj konto")
        label1 = QLabel("Wybierz właściwą opcję:")

        types = ['mam konto', 'nie mam konta']

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(50, 50, 100, 35)
        self.comboBox.addItems(types)

        self.vbox = QGridLayout()
        self.vbox.addWidget(label1,0,0)
        self.vbox.addWidget(button1, 1, 0)
        self.vbox.addWidget(self.comboBox,1,1)
        self.vbox.addWidget(button2, 2, 0)
        self.vbox.addWidget(button3, 3, 0)

        self.setLayout(self.vbox)
        button1.clicked.connect(self.button1)
        button2.clicked.connect(self.button2)
        button3.clicked.connect(self.button3)

    def button1(self):
        # print('Button 1 was clicked')
        # car_number = "AAH88TV"
        if(self.comboBox.currentIndex()==0):
            rejestracja, numer = self.openDialog1()
            if(rejestracja!=None):
                # rejestracja = "AAH88TV"
                # numer = "03102968983"
                # numer="US96315"
                flag1=False
                if(len(rejestracja)<5 or len(rejestracja)>8):
                    msg = "Wprowadzono nieprawidłową rejestrację. Spróbuj ponownie"
                    self.ErrorINFO(msg)
                else:
                    car_result=self.lookforClientbyCar(rejestracja)
                    if(len(car_result)==1):
                        flag1=True
                    else:
                        msg = f"Nie ma w bazie pojazdu o numerze rejestracyjnym: {rejestracja}. Spróbuj ponownie"
                        self.ErrorINFO(msg)

                if(len(numer)!=11 and len(numer)!=7):
                    msg = "Wprowadzono nieprawidłowy identyfikator. Spróbuj ponownie"
                    self.ErrorINFO(msg)
                else:
                    if(len(numer)==11):
                        data = self.lookforClientbyPesel(int(numer))
                        if (len(data) != 1):
                            msg = "Nie ma takiego klienta w bazie. Spróbuj ponownie"
                            self.ErrorINFO(msg)
                        else:
                            if(flag1):
                                exit, id_pobytu=self.updatePobyt(rejestracja)
                                if(exit):
                                    saldo = data[0][4]
                                    Title = "Sukces"
                                    msg = f"Pobyt zakończony sukcesem. Stan twojego konta wynosi {saldo}."
                                    self.ErrorINFO(msg, Title)
                                else:
                                    msg = f"Nie udało się znaleźć niezakończonego pobytu pojazdu o rejestracji: {rejestracja}."
                                    self.ErrorINFO(msg)
                            else:
                                pass
                    else:
                        data = self.lookforClientbyCard(numer)
                        if (len(data) != 1):
                            msg = "Nie ma takiego klienta w bazie. Spróbuj ponownie"
                            self.ErrorINFO(msg)
                        else:
                            if (flag1):
                                exit, id_pobytu = self.updatePobyt(rejestracja)
                                if (exit):
                                    saldo = data[0][4]
                                    Title = "Sukces"
                                    msg = f"Pobyt zakończony sukcesem. Stan twojego konta wynosi {saldo}."
                                    self.ErrorINFO(msg, Title)
                                else:
                                    msg = f"Nie udało się znaleźć niezakończonego pobytu pojazdu o rejestracji: {rejestracja}."
                                    self.ErrorINFO(msg)
                            else:
                                pass


        else:
            rejestracja, option=self.openDialog12()
            if(rejestracja!=None):
                flag1 = False
                if (len(rejestracja) < 5 or len(rejestracja) > 8):
                    msg = "Wprowadzono nieprawidłową rejestrację. Spróbuj ponownie"
                    self.ErrorINFO(msg)
                else:
                    car_result = self.lookforClientbyCar(rejestracja)
                    if (len(car_result) == 1):
                        flag1 = True
                    else:
                        msg = f"Nie ma w bazie pojazdu o numerze rejestracyjnym: {rejestracja}. Spróbuj ponownie"
                        self.ErrorINFO(msg)

                flag2=False
                if(flag1):
                    exit, id_pobytu = self.updatePobyt(rejestracja)
                    if (exit):
                        flag2=True
                    else:
                        msg = f"Nie udało się znaleźć niezakończonego pobytu pojazdu o rejestracji: {rejestracja}."
                        self.ErrorINFO(msg)

                if(flag1):
                    exit, id_pobytu = self.updatePobyt(rejestracja)
                    if(flag2):
                        if(option==0):
                            naleznosc=self.getlNaleznosc(id_pobytu)
                            msg = f"Należność za usługę wynosi: {naleznosc} złotych. W celu zakończenia przyłóż kartę."
                            Title="Instrukcja"
                            self.ErrorINFO(msg, Title)
                            Title = "Sukces"
                            msg = f"Pobyt zakończony sukcesem. Miłego dnia."
                            self.ErrorINFO(msg, Title)
                        else:
                            naleznosc = self.getlNaleznosc(id_pobytu)
                            status=False

                            msg = f"Należność za usługę wynosi: {naleznosc} złotych. W celu zakończenia wprowadź kwotę równą lub większą."
                            Title = "Instrukcja"
                            self.ErrorINFO(msg, Title)
                            while (status == False):
                                kwota=self.openDialog13()
                                isd=kwota.isdigit()
                                if(isd):
                                    kwota=int(kwota)/100
                                    dif=kwota-naleznosc
                                    if(dif>=0):
                                        msg=f"Wydana reszta: {dif} złotych. Miłego dnia."
                                        Title= "Sukces"
                                        self.ErrorINFO(msg,Title)
                                        status=True
                                    else:
                                        msg=f"Brakuje jeszcze {-dif} złotych. Wprowadż tą kwotę aby zakończyć"
                                        Title = "Sukces"
                                        self.ErrorINFO(msg, Title)
                                        naleznosc=-dif
                                else:
                                    msg = f"Kwota powinna być dodatnią cyfrą. Spróbuj ponownie."
                                    self.ErrorINFO(msg)



    def button2(self):
        # print('Button 2 was clicked')
        pesel= self.openDialog2()
        if(pesel==None):
            return
        else:
            # car_number = "AAH88TV"
            # pesel = "03102968983"
            if (len(pesel) != 11):
                msg = "Wprowadzono nieprawidłowe dane. Spróbuj ponownie"
                self.ErrorINFO(msg)
            else:
                data=self.lookforClientbyPesel(int(pesel))
                if(len(data)!=1):
                    msg = "Nie ma takiego klienta w bazie. Spróbuj ponownie"
                    self.ErrorINFO(msg)
                else:
                    saldo=data[0][4]
                    Title="Sukces"
                    msg=f"Stan konta o numerze PESEL:{pesel} wynosi {saldo}."
                    self.ErrorINFO(msg,Title)


    def button3(self):
        # print("Button 3 was clicked")
        kwota, pesel, opcja = self.openDialog3()
        if(kwota==None):
            return
        else:
            # car_number = "AA11111"
            # pesel = "03102968983"
            if (len(pesel) != 11):
                msg = "Wprowadzono nieprawidłowe dane. Spróbuj ponownie"
                self.ErrorINFO(msg)
            else:
                data=self.lookforClientbyPesel(int(pesel))
                if(len(data)!=1):
                    msg = "Nie ma takiego klienta w bazie. Spróbuj ponownie"
                    self.ErrorINFO(msg)
                else:
                    if(kwota.isdigit()):
                        saldo=data[0][4]
                        kwota=int(kwota)
                        kwota=kwota/100
                        total=kwota+saldo
                        self.updateSaldo(total,pesel)
                        Title="Sukces"
                        msg=f"Stan konta o numerze PESEL:{pesel} po doładowaniu wynosi {total}."
                        self.ErrorINFO(msg,Title)
                    else:
                        msg = "Kwota doładowania musi byc liczbą dodatnią. Spróbuj ponownie."
                        self.ErrorINFO(msg)



    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def getCardID(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Wprowadź numer karty:')
        if ok:
            self.IDt.setText(str(text))


    def openDialog1(self):
        msg1 = "Wprowadź rejestrację"
        msg2="Wprowadź PESEL lub numer karty"
        dialog1 = InputDialog(msg1,msg2,False)
        dialog1.show()
        output = dialog1.exec()
        if (output):
            rejestracja, numer_identyfikacyjny = dialog1.getInputs()
            return (rejestracja, numer_identyfikacyjny)
        else:
            return (None,None)

    def openDialog12(self):
        msg1 = "Wprowadź rejestrację"
        dialog1 = InputDialog3(msg1, True)
        dialog1.show()
        output = dialog1.exec()
        if (output):
            rejestracja,option= dialog1.getInputs()
            return (rejestracja, option)
        else:
            return (None,None)

    def openDialog13(self):
        msg1 = "Wprowadź kwotę w groszach"
        dialog1 = InputDialog3(msg1, False)
        dialog1.show()
        output=dialog1.exec()
        if(output):
            kwota= dialog1.getInputs()
            return kwota
        else:
            return None


    def openDialog2(self):
        msg = "Wprowadż numer PESEL"
        dialog1 = InputDialog3(msg, False)
        dialog1.show()
        output=dialog1.exec()
        if (output):
            PESEL = dialog1.getInputs()
            return PESEL
        else:
            return None

    def openDialog3(self):
        msg1 = "Wprowadź kwotę w groszach"
        msg2 = "Wprowadź PESEL"
        dialog1 = InputDialog(msg1,msg2)
        dialog1.show()
        output=dialog1.exec()
        if (output):
            kwota, pesel, opcja = dialog1.getInputs()
            return (kwota, pesel, opcja)
        else:
            return (None, None, None)



    def lookforClientbyCard(self, card_number):
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql = "SELECT * FROM konta WHERE kod_karty=%s"
        cursor.execute(sql, [card_number])
        data = cursor.fetchall()
        db.close()
        return data

    def lookforClientbyPesel(self, pesel):
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql = "SELECT * FROM konta WHERE pesel=%s"
        cursor.execute(sql, [pesel])
        data = cursor.fetchall()
        db.close()
        return data

    def lookforClientbyCar(self, car_number):
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql = "SELECT * FROM pojazdy WHERE rejestracja=%s"
        cursor.execute(sql, [car_number])
        data = cursor.fetchall()
        db.close()
        return data


    def getStrefabyBramkaID(self):
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql = "SELECT strefy_id FROM bramki WHERE id=%s"
        cursor.execute(sql, [str(ID_NUMBER)])
        data = cursor.fetchone()
        db.close()
        data = data[0]
        return data

    def getStartTime(self):
        now = QDate.currentDate()
        date1 = now.toString(Qt.ISODate)
        time = QTime.currentTime()
        time1 = time.toString(Qt.DefaultLocaleLongDate)
        total = f"{date1} {time1}"
        return total



    def getIDKontabyCard(self, card_number):
        id_klienta = self.lookforClientbyCard(card_number)
        id_klienta = id_klienta[0][0]
        return id_klienta

    def getIDKontabyPesel(self, pesel):
        id_klienta = self.lookforClientbyPesel(pesel)
        id_klienta = id_klienta[0][0]
        return id_klienta

    def ErrorINFO(self, msg, Title="Niepowodzenie"):
        QMessageBox.about(self, Title, msg)


    def getKodMiejsca(self, id_pobytu):
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql = "SELECT kod FROM miejsca WHERE id IN (SELECT miejsca_id FROM z_parkowaniem WHERE id=%s) "
        cursor.execute(sql, [str(id_pobytu)])
        data = cursor.fetchone()
        data = data[0]
        db.close()
        return data

    def updateSaldo(self,nowe_saldo, pesel):
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql = "UPDATE konta SET saldo=%s WHERE pesel=%s"
        cursor.execute(sql, [nowe_saldo, pesel])
        db.commit()
        db.close()

    def updatePobyt(self, rejestracja):
        time_start = self.getStartTime()
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql1 = "SELECT id FROM pobyty WHERE pojazdy_rejestracja=%s and godzina_zakonczenia is NULL"
        cursor.execute(sql1, [rejestracja])
        data = cursor.fetchone()
        if(data!=None):
            id = data[0]
            sql2 = "UPDATE pobyty SET godzina_zakonczenia=%s, wyjazdowe_bramki_id=%s WHERE id=%s"
            cursor.execute(sql2, [time_start, ID_NUMBER, id])
            db.commit()
            exit=(True, id)
        else:
            exit=(False,None)
        db.close()
        return exit

    def getlNaleznosc(self, id_pobytu):
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql = "SELECT należność FROM pobyty WHERE id=%s"
        cursor.execute(sql, [str(id_pobytu)])
        data = cursor.fetchone()
        db.close()
        return data[0]


class InputDialog(QDialog):
    def __init__(self, msg1,msg2,opt=True, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Wprowadź dane")
        self.opt=opt
        self.kwota = QLineEdit(self)
        self.pesel = QLineEdit(self)
        if(opt):
            types = ['karta', 'gotówka']
            self.comboBox = QComboBox(self)
            self.comboBox.setGeometry(50, 50, 100, 35)
            self.comboBox.addItems(types)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow(msg1, self.kwota)
        layout.addRow(msg2, self.pesel)
        if(opt):
            layout.addRow("Wybierz opcję ", self.comboBox)

        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        if(self.opt):
            return (self.kwota.text(), self.pesel.text(), self.comboBox.currentIndex())
        else:
            return (self.kwota.text(), self.pesel.text())


class InputDialog3(QDialog):
    def __init__(self, msg2,opt=False, parent=None):
        super().__init__(parent)
        self.opt=opt
        self.setWindowTitle("Wprowadź dane")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);
        self.pesel = QLineEdit(self)
        if (opt):
            types = ['karta', 'gotówka']
            self.comboBox = QComboBox(self)
            self.comboBox.setGeometry(50, 50, 100, 35)
            self.comboBox.addItems(types)

        layout = QFormLayout(self)
        layout.addRow(msg2, self.pesel)
        if (opt):
            layout.addRow("Wybierz opcję ", self.comboBox)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        if (self.opt):
            return (self.pesel.text(), self.comboBox.currentIndex())
        else:
            return self.pesel.text()


if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

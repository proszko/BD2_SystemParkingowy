import sys
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


ID_NUMBER=4

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bramka wjazdowa")
        self.resize(700,400)
        self.center()
        self.main_window_init()

    def main_window_init(self):

        self.setFont(QFont('SanSerif',16))
        buttonCard = QPushButton("Posiadam kartę klienta")
        buttonNoCard = QPushButton("Nie posiadam karty klienta, nie mam konta")
        buttonNoCard2 = QPushButton("Nie posiadam karty klienta ale mam konto")

        self.text=f"Wybierz właściwą opcję"
        QLabel(self.text,self)

        self.vbox = QGridLayout()
        self.vbox.addWidget(buttonCard, 1, 0)
        self.vbox.addWidget(buttonNoCard2, 2, 0)
        self.vbox.addWidget(buttonNoCard,3, 0)

        self.setLayout(self.vbox)
        buttonCard.clicked.connect(self.button1)
        buttonNoCard2.clicked.connect(self.button2)
        buttonNoCard.clicked.connect(self.button3)

    def button1(self):
        print('Button 1 was clicked')
        car_number, card_number, Option=self.openDialog1()
        # car_number="AAH88TV"
        # card_number="US96315"
        check=self.decideIfInformationisComplete(car_number, card_number)
        if(check):
            if(Option):
                if(self.areAvailablePlaces(car_number)):
                    id_pobytu=self.SuccessProcess(Option, car_number, card_number)
                else:
                    Title = "Niepowodzenie"
                    msg=f"Brak wolnych miejsc w wybranej strefie.\nSpróbuj w innej bramce.\n Przepraszamy!"
                    self.ErrorINFO(msg,Title)
            else:
                id_pobytu=self.SuccessProcess(Option, car_number, card_number)
        else:
            print(f"Braki informacji")
        if(Option):
            kod_miejsca=self.getKodMiejsca(id_pobytu)
            title="Sukces"
            msg=f"Proces przebiegł prawidłowo. Przyznano miejsce o kodzie: {kod_miejsca}."
            self.ErrorINFO(msg,title)
        else:
            title = "Sukces"
            msg = f"Proces przebiegł prawidłowo."
            self.ErrorINFO(msg, title)


    def button2(self):
        print('Button 2 was clicked')
        car_number, pesel, Option = self.openDialog2()
        # car_number = "AAH88TV"
        # pesel = "03102968983"
        check=self.decideIfInformationisComplete2(car_number, pesel)
        if (check):
            if (Option):
                if (self.areAvailablePlaces(car_number)):
                    id_pobytu=self.SuccessProcess(Option, car_number, pesel)
                else:
                    Title = "Niepowodzenie"
                    msg = f"Brak wolnych miejsc w wybranej strefie.\nSpróbuj w innej bramce.\n Przepraszamy!"
                    self.ErrorINFO(msg, Title)
            else:
                id_pobytu=self.SuccessProcess(Option, car_number, pesel)
        else:
            print(f"Braki informacji")

        if (Option):
            kod_miejsca = self.getKodMiejsca(id_pobytu)
            title = "Sukces"
            msg = f"Proces przebiegł prawidłowo. Przyznano miejsce o kodzie: {kod_miejsca}."
            self.ErrorINFO(msg, title)
        else:
            title = "Sukces"
            msg = f"Proces przebiegł prawidłowo."
            self.ErrorINFO(msg, title)

    def button3(self):
        print("Button 3 was clicked")
        car_number, pesel, Option = self.openDialog3()
        # car_number = "AA11111"
        # pesel = "00002968983"
        check = self.decideIfInformationisComplete3(car_number, pesel)
        if (check):
            if (Option):
                if (self.areAvailablePlaces(car_number)):
                    id_pobytu=self.SuccessProcess(Option, car_number, pesel,False)
                else:
                    Title = "Niepowodzenie"
                    msg = f"Brak wolnych miejsc w wybranej strefie.\nSpróbuj w innej bramce.\n Przepraszamy!"
                    self.ErrorINFO(msg, Title)
            else:
                id_pobytu=self.SuccessProcess(Option, car_number, pesel, False)
        else:
            print(f"Braki informacji")

        if (Option):
            kod_miejsca = self.getKodMiejsca(id_pobytu)
            title = "Sukces"
            msg = f"Proces przebiegł prawidłowo. Przyznano miejsce o kodzie: {kod_miejsca}."
            self.ErrorINFO(msg, title)
        else:
            title = "Sukces"
            msg = f"Proces przebiegł prawidłowo."
            self.ErrorINFO(msg, title)

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


    def openSecondDialog(self):
        mydialog=QDialog()
        mydialog.setModal(True)
        mydialog.exec()

    def openDialog1(self):
        msg="Wprowadź kod karty"
        dialog1=InputDialog(msg)
        dialog1.show()
        if dialog1.exec():
            rejestracja, nr_karty = dialog1.getInputs()
        option = dialog1.getOption()
        return (rejestracja, nr_karty, option)

    def openDialog2(self):
        msg = "Wprowadż numer PESEL"
        dialog1 = InputDialog(msg)
        dialog1.show()
        if dialog1.exec():
            rejestracja, PESEL = dialog1.getInputs()
        option = dialog1.getOption()
        return (rejestracja, PESEL, option)

    def openDialog3(self):
        msg = "Wprowadż numer PESEL"
        dialog1 = InputDialog(msg)
        dialog1.show()
        if dialog1.exec():
            rejestracja, pesel = dialog1.getInputs()
        option = dialog1.getOption()
        return (rejestracja, pesel, option)

    def nowyPojazdDialog(self):
        opt = False
        dialog1 = InputDialog2(opt)
        dialog1.show()
        if dialog1.exec():
            rejestracja, model = dialog1.getInputs()
        pojazd_id = dialog1.getComboValue()
        self.addPojazd(rejestracja,pojazd_id,model)
        Title="Sukces"
        msg="Pomyślnie dodano pojazd. Proszę ponownie spróbować zarejestrować wjazd."
        self.ErrorINFO(msg,Title)

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

    def decideIfInformationisComplete(self,car_number, card_number):
        card_result=self.lookforClientbyCard(card_number)
        car_result=self.lookforClientbyCar(car_number)
        iscomplete=False
        if(len(car_result)==1):
            if(len(card_result)==1):
                if(card_result[0][-1]=="1"):
                    iscomplete=True
                else:
                    msg = "Twoje konto jest niekatywne.\n Aby dowiedzieć się więcej udaj się do punktu informacji."
                    self.ErrorINFO(msg)
            else:
                msg = "Nie znaleziono konta w systemie z przypisaną kartą o podanym kodzie. " \
                      "Aby dowiedzieć się więcej udaj się do punktu informacji."
                self.ErrorINFO(msg)
        else:
            msg = "Nie znaleziono takiego pojazdu w systemie. Należy go dodać."
            self.ErrorINFO(msg)
            self.nowyPojazdDialog()

        return iscomplete

    def decideIfInformationisComplete2(self,car_number, pesel):
        card_result=self.lookforClientbyPesel(pesel)
        car_result=self.lookforClientbyCar(car_number)
        iscomplete=False
        if(len(car_result)==1):
            if(len(card_result)==1):
                if(card_result[0][-1]=="1"):
                    iscomplete=True
                else:
                    msg = "Twoje konto jest niekatywne.\n Aby dowiedzieć się więcej udaj się do punktu informacji."
                    self.ErrorINFO(msg)
            else:
                msg = "Nie znaleziono konta w systemie podanym numerze PESEL. " \
                      "Aby dowiedzieć się więcej udaj się do punktu informacji."
                self.ErrorINFO(msg)
        else:
            msg = "Nie znaleziono takiego pojazdu w systemie. Należy go dodać."
            self.ErrorINFO(msg)
            self.nowyPojazdDialog()

        return iscomplete

    def decideIfInformationisComplete3(self, car_number, pesel):
        car_result = self.lookforClientbyCar(car_number)
        iscomplete = False
        if (len(car_result) == 1):
            iscomplete = True
        else:
            msg = "Nie znaleziono takiego pojazdu w systemie. Należy go dodać."
            self.ErrorINFO(msg)
            self.nowyPojazdDialog()

        return iscomplete

    def SuccessProcess(self, Option, car_number, card_number, all=True):
        if(all):
            if(card_number.isdigit()):
                id_konta=self.getIDKontabyPesel(card_number)
            else:
                id_konta= self.getIDKontabyCard(card_number)
            if(Option):
                id_pobytu=self.addPobyt(id_konta,ID_NUMBER,car_number,"z_parkowaniem")
            else:
                id_pobytu=self.addPobyt(id_konta,ID_NUMBER, car_number, "bez_parkowania")
        else:
            if (Option):
                id_pobytu=self.addPobyt2( ID_NUMBER, car_number, "z_parkowaniem")
            else:
                id_pobytu=self.addPobyt2(ID_NUMBER, car_number, "bez_parkowania")
        return id_pobytu


    def getStrefabyBramkaID(self):
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql = "SELECT strefy_id FROM bramki WHERE id=%s"
        cursor.execute(sql, [str(ID_NUMBER)])
        data = cursor.fetchone()
        db.close()
        data=data[0]
        return data

    def getStartTime(self):
        now = QDate.currentDate()
        date1=now.toString(Qt.ISODate)
        time = QTime.currentTime()
        time1=time.toString(Qt.DefaultLocaleLongDate)
        total=f"{date1} {time1}"
        return total

    def chekIFthereAreAvialablePalces(self,id_strefy, id_typu_pojazdu):
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql = "SELECT miejsca, miejsca_zajete FROM pojemności WHERE strefy_id=%s AND " \
              "typy_pojazdów_id=%s"
        cursor.execute(sql, [str(id_strefy), str(id_typu_pojazdu)])
        data = cursor.fetchone()
        db.close()
        data = data[0]-data[1]
        if(data>0):
            return True
        else:
            return False

    def areAvailablePlaces(self,car_number):
        car_result=self.lookforClientbyCar(car_number)
        id_strefy=self.getStrefabyBramkaID()
        id_typu_pojazdu=car_result[0][1]
        isPlace=self.chekIFthereAreAvialablePalces(id_strefy,id_typu_pojazdu)
        return isPlace

    def addPobyt(self,id_konta,id_bramki_wjazdowej, rejestracja, opcja):
        time_start =self.getStartTime()
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql = "INSERT INTO pobyty (godzina_rozpoczecia,konta_id, wjazdowe_bramki_id, selektor, pojazdy_rejestracja) " \
              "VALUES (%s,%s,%s,%s,%s) "
        cursor.execute(sql, [time_start, str(id_konta),str(id_bramki_wjazdowej),opcja,rejestracja])
        db.commit()
        sql = "SELECT LAST_INSERT_ID()"
        cursor.execute(sql)
        data = cursor.fetchone()
        db.close()
        return data[0]

    def addPobyt2(self,id_bramki_wjazdowej, rejestracja, opcja):
        time_start =self.getStartTime()
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql = "INSERT INTO pobyty (godzina_rozpoczecia, wjazdowe_bramki_id, selektor, pojazdy_rejestracja) " \
              "VALUES (%s,%s,%s,%s) "
        cursor.execute(sql, [time_start,str(id_bramki_wjazdowej),opcja,rejestracja])
        db.commit()
        sql = "SELECT LAST_INSERT_ID()"
        cursor.execute(sql)
        data = cursor.fetchone()
        db.close()
        return data[0]

    def getIDKontabyCard(self,card_number):
        id_klienta=self.lookforClientbyCard(card_number)
        id_klienta=id_klienta[0][0]
        return id_klienta

    def getIDKontabyPesel(self,pesel):
        id_klienta=self.lookforClientbyPesel(pesel)
        id_klienta=id_klienta[0][0]
        return id_klienta

    def ErrorINFO(self,msg,Title="Niepowodzenie"):
        QMessageBox.about(self,Title, msg)

    def addPojazd(self, rejestracja, typ_pojazdu_id, model):
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql = "INSERT INTO pojazdy (rejestracja,typy_pojazdów_id,model) " \
              "VALUES (%s,%s,%s) "
        cursor.execute(sql, [rejestracja, str(typ_pojazdu_id), model])
        db.commit()
        db.close()

    def getKodMiejsca(self, id_pobytu):
        db = MySQLdb.connect("localhost", "root", "wpisz_haslo", "database_test")
        cursor = db.cursor()
        sql = "SELECT kod FROM miejsca WHERE id IN (SELECT miejsca_id FROM z_parkowaniem WHERE id=%s) "
        cursor.execute(sql,[str(id_pobytu)])
        data=cursor.fetchone()
        data=data[0]
        db.close()
        return data

class InputDialog(QDialog):
    def __init__(self, msg2,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Wprowadź dane")

        self.rejestracja = QLineEdit(self)
        self.numerIDkarty = QLineEdit(self)
        self.checkbox = QCheckBox("z parkowaniem")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("Wpisz rejestrację", self.rejestracja)
        layout.addRow(msg2, self.numerIDkarty)
        layout.addRow("", self.checkbox)

        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)


    def getInputs(self):
        return (self.rejestracja.text(), self.numerIDkarty.text())

    def getOption(self):
        if(self.checkbox.isChecked()):
            return True
        else:
            return False


class InputDialog2(QDialog):
    def __init__(self,opt,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Wprowadź dane")

        types= ['osobowy', 'ciężarowy', 'autobus', 'taksówka', 'jednoślad','osobowy z przyczepą', 'naczepa ciężarowa', 'maszyna rolnicza']

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(50, 50, 100, 35)
        self.comboBox.addItems(types)
        self.rejestracja = QLineEdit(self)
        self.model = QLineEdit(self)
        if(opt):
            self.checkbox = QCheckBox("z parkowaniem")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("Wpisz rejestrację", self.rejestracja)
        layout.addRow("Wpisz model pojazdu", self.model)
        layout.addRow("Wybierz typ pojazdu", self.comboBox)
        if(opt):
            layout.addRow("", self.checkbox)

        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)


    def getInputs(self):
        return (self.rejestracja.text(), self.model.text())

    def getOption(self):
        if(self.checkbox.isChecked()):
            return True
        else:
            return False

    def getComboValue(self):
        return self.comboBox.currentIndex()+1



if __name__ == "__main__":


   app = QApplication([])
   window = MainWindow()
   window.show()
   sys.exit(app.exec_())




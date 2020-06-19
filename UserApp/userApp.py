import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from tkinter import *


class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("User Application")
        self.button1 = Button(self, text="Stan zapełnienia parkingów", command=self.park_zone_status)
        self.button1.pack(fill=BOTH)
        self.button2 = Button(self, text="Stan kas bramek wyjazdowych", command=self.gate_money_status)
        self.button2.pack(fill=BOTH)
        self.button3 = Button(self, text="Zarządzanie kontami klienckimi", command=self.account_management)
        self.button3.pack(fill=BOTH)
        self.button4 = Button(self, text="Lista klientów z debetem na koncie klienckim",
                              command=self.overdraft_client_list)
        self.button4.pack(fill=BOTH)
        self.button5 = Button(self, text="Generuj listę zaległości", command=self.generate_money_list)
        self.button5.pack(fill=BOTH)
        self.pack()
        self.master.resizable(False, False)

    def park_zone_status(self):
        newWindow = Toplevel(self.master)
        app = ParkWindow(newWindow)

    def gate_money_status(self):
        newWindow = Toplevel(self.master)
        app = MoneyWindow(newWindow)

    def account_management(self):
        newWindow = Toplevel(self.master)
        app = AccountWindow(newWindow)
        app.draw_contents()

    def overdraft_client_list(self):
        newWindow = Toplevel(self.master)
        app = OverdraftWindow(newWindow)

    def generate_money_list(self):
        f = open("lista.txt", "w")
        db = MySQLdb.connect("localhost", "root", "BD2projekt!", "bd2_schema")
        cursor = db.cursor()
        sql1 = "SELECT konta.pesel, konta.saldo FROM konta \
                WHERE saldo < 0.0 ORDER BY konta.saldo;"
        try:
            cursor.execute(sql1)
            result = cursor.fetchall()
            field_names = [i[0] for i in cursor.description]
            length = len(field_names)
            for j in range(length):
                f.write(field_names[j])
                f.write("\t\t")
            for idx1, row in enumerate(result):
                f.write("\n")
                for idx2, column in enumerate(row):
                    f.write(str(column))
                    f.write("\t")
        except:
            print("Error: Unable to fetch data")
        db.close()
        f.close()
        print("Wygenerowano listę zaległości - plik lista.txt")


class AccEditionWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Wprowadź dane konta")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.master.geometry("970x510")
        self.grid()
        self.master.resizable(False, False)

    def draw_contents(self, field_names):
        pass

    def confirm_button_fun(self):
        pass

    def cancel_button_fun(self):
        pass


class AccountWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Zarządzanie kontami klienckimi")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.master.geometry("970x510")
        self.grid()
        self.master.resizable(False, False)

    def draw_contents(self):
        canvas = Canvas(self, width=950, height=500)
        canvas.rowconfigure(0, weight=1)
        canvas.columnconfigure(0, weight=1)
        canvas.grid(row=0, column=0, sticky="nsew")
        canvasFrame = Frame(canvas)
        canvas.create_window(0, 0, window=canvasFrame, anchor='nw')
        db = MySQLdb.connect("localhost", "root", "BD2projekt!", "bd2_schema")
        cursor = db.cursor()
        sql1 = "SELECT konta.pesel, konta.nazwisko, konta.imię, konta.saldo, \
                konta.telefon, konta.email, ulgi.nazwa AS nazwa_ulgi, konta.kod_karty, \
                IF(konta.aktywne = 1, 'aktywne', 'nieaktywne') AS stan_konta \
                FROM konta LEFT JOIN ulgi ON konta.ulgi_id = ulgi.id \
                ORDER BY konta.aktywne DESC, konta.nazwisko ASC, konta.imię ASC;"
        try:
            cursor.execute(sql1)
            result = cursor.fetchall()
            field_names = [i[0] for i in cursor.description]
            j = 0
            length = len(field_names)
            for j in range(length):
                label1 = Label(canvasFrame, text=field_names[j], font="bold", bg="light grey")
                label1.grid(row=0, column=j, sticky="ew", padx=1, pady=1)
            button1 = Button(canvasFrame, bg="tomato", text="Dodaj konto", command=self.add_account)
            button1.grid(row=0, column=j + 1, sticky="ew", padx=1, pady=1)
            for idxr, row in enumerate(result):
                idxc = 0
                for idxc, column in enumerate(row):
                    label1 = Label(canvasFrame, text=column)
                    label1.grid(row=idxr + 1, column=idxc, padx=1, pady=1)
                button1 = Button(canvasFrame, bg="light blue", text="Edytuj konto")
                button1.grid(row=idxr + 1, column=idxc + 1, sticky="ew", padx=1, pady=1)
                button1.configure(command=lambda pesel=result[idxr][0]: self.edit_account(pesel))
        except:
            print("Error: Unable to fetch data")
        db.close()
        scroll = Scrollbar(self, orient=VERTICAL)
        scroll.config(command=canvas.yview)
        canvas.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky="ns")
        self.update()
        canvas.configure(scrollregion=canvas.bbox("all"))

    def edit_account(self, pesel):
        pass

    def add_account(self):
        pass


class ParkWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Stan zapełnienia parkingów")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.master.geometry("720x510")
        self.grid()
        canvas = Canvas(self, width=700, height=500)
        canvas.rowconfigure(0, weight=1)
        canvas.columnconfigure(0, weight=1)
        canvas.grid(row=0, column=0, sticky="nsew")
        canvasFrame = Frame(canvas)
        canvas.create_window(0, 0, window=canvasFrame, anchor='nw')
        db = MySQLdb.connect("localhost", "root", "BD2projekt!", "bd2_schema")
        cursor = db.cursor()
        sql1 = "SELECT strefy.kod, strefy.nazwa, \
                sum(if(miejsca.czy_wolne = 1, 1, 0)) as liczba_wolnych_miejsc, \
                sum(if(miejsca.czy_wolne = 0, 1, 0)) as liczba_zajetych_miejsc \
                FROM strefy INNER JOIN miejsca ON strefy.id = miejsca.strefy_id \
                GROUP BY strefy.nazwa ORDER BY strefy.nazwa;"
        try:
            cursor.execute(sql1)
            result = cursor.fetchall()
            field_names = [i[0] for i in cursor.description]
            length = len(field_names)
            for j in range(length):
                label1 = Label(canvasFrame, text=field_names[j], font="bold", bg="light grey")
                label1.grid(row=0, column=j, sticky="ew", padx=1, pady=1)
            for idxr, row in enumerate(result):
                for idxc, column in enumerate(row):
                    label1 = Label(canvasFrame, text=column)
                    label1.grid(row=idxr + 1, column=idxc, padx=1, pady=1)
        except:
            print("Error: Unable to fetch data")
        db.close()
        scroll = Scrollbar(self, orient=VERTICAL)
        scroll.config(command=canvas.yview)
        canvas.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky="ns")
        self.update()
        canvas.configure(scrollregion=canvas.bbox("all"))
        self.master.resizable(False, False)


class MoneyWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Stan kas bramek wyjazdowych")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.master.geometry("1220x510")
        self.grid()
        canvas = Canvas(self, width=1200, height=500)
        canvas.rowconfigure(0, weight=1)
        canvas.columnconfigure(0, weight=1)
        canvas.grid(row=0, column=0, sticky="nsew")
        canvasFrame = Frame(canvas)
        canvas.create_window(0, 0, window=canvasFrame, anchor='nw')
        db = MySQLdb.connect("localhost", "root", "BD2projekt!", "bd2_schema")
        cursor = db.cursor()
        sql1 = "SELECT bramki.nazwa, strefy.nazwa AS strefa, wyjazdowe.count_1gr, \
                wyjazdowe.count_2gr, wyjazdowe.count_5gr, wyjazdowe.count_10gr, \
                wyjazdowe.count_20gr, wyjazdowe.count_50gr, wyjazdowe.count_1zl, \
                wyjazdowe.count_2zl, wyjazdowe.count_5zl FROM bramki \
                INNER JOIN strefy ON bramki.strefy_id = strefy.id \
                INNER JOIN wyjazdowe ON bramki.id = wyjazdowe.id \
                ORDER BY strefy.nazwa, bramki.nazwa;"
        try:
            cursor.execute(sql1)
            result = cursor.fetchall()
            field_names = [i[0] for i in cursor.description]
            length = len(field_names)
            for j in range(length):
                label1 = Label(canvasFrame, text=field_names[j], font="bold", bg="light grey")
                label1.grid(row=0, column=j, sticky="ew", padx=1, pady=1)
            for idxr, row in enumerate(result):
                for idxc, column in enumerate(row):
                    label1 = Label(canvasFrame, text=column)
                    label1.grid(row=idxr + 1, column=idxc, padx=1, pady=1)
        except:
            print("Error: Unable to fetch data")
        db.close()
        scroll = Scrollbar(self, orient=VERTICAL)
        scroll.config(command=canvas.yview)
        canvas.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky="ns")
        self.update()
        canvas.configure(scrollregion=canvas.bbox("all"))
        self.master.resizable(False, False)


class OverdraftWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Lista klientów z debetem na koncie klienckim")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.master.geometry("620x510")
        self.grid()
        canvas = Canvas(self, width=600, height=500)
        canvas.rowconfigure(0, weight=1)
        canvas.columnconfigure(0, weight=1)
        canvas.grid(row=0, column=0, sticky="nsew")
        canvasFrame = Frame(canvas)
        canvas.create_window(0, 0, window=canvasFrame, anchor='nw')
        db = MySQLdb.connect("localhost", "root", "BD2projekt!", "bd2_schema")
        cursor = db.cursor()
        sql1 = "SELECT konta.pesel, konta.nazwisko, konta.imię, konta.saldo, \
                konta.telefon, konta.email FROM konta \
                WHERE saldo < 0.0 ORDER BY konta.saldo, konta.nazwisko, konta.imię;"
        try:
            cursor.execute(sql1)
            result = cursor.fetchall()
            field_names = [i[0] for i in cursor.description]
            length = len(field_names)
            for j in range(length):
                label1 = Label(canvasFrame, text=field_names[j], font="bold", bg="light grey")
                label1.grid(row=0, column=j, sticky="ew", padx=1, pady=1)
            for idxr, row in enumerate(result):
                for idxc, column in enumerate(row):
                    label1 = Label(canvasFrame, text=column)
                    label1.grid(row=idxr + 1, column=idxc, padx=1, pady=1)
        except:
            print("Error: Unable to fetch data")
        db.close()
        scroll = Scrollbar(self, orient=VERTICAL)
        scroll.config(command=canvas.yview)
        canvas.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky="ns")
        self.update()
        canvas.configure(scrollregion=canvas.bbox("all"))
        self.master.resizable(False, False)


def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()

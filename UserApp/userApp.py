import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("User Application")
        self.label1 = tk.Label(self, text="Podsumowanie danych w systemie:", font="bold", bg="light grey")
        self.label1.pack(fill=tk.BOTH)
        self.button1 = tk.Button(self, text="Stan zapełnienia parkingów", command=self.park_zone_status)
        self.button1.pack(fill=tk.BOTH)
        self.button2 = tk.Button(self, text="Stan kas bramek wyjazdowych", command=self.gate_money_status)
        self.button2.pack(fill=tk.BOTH)
        self.button3 = tk.Button(self, text="Lista klientów z debetem na koncie klienckim",
                                 command=self.overdraft_client_list)
        self.button3.pack(fill=tk.BOTH)
        self.button4 = tk.Button(self, text="Generuj listę zaległości", command=self.generate_money_list)
        self.button4.pack(fill=tk.BOTH)
        self.label2 = tk.Label(self, text="Zarządzanie systemem:", font="bold", bg="light grey")
        self.label2.pack(fill=tk.BOTH)
        self.button5 = tk.Button(self, text="Zarządzanie kontami klienckimi", command=self.account_management)
        self.button5.pack(fill=tk.BOTH)
        self.button6 = tk.Button(self, text="Zarządzanie ulgami", command=self.discount_management)
        self.button6.pack(fill=tk.BOTH)
        self.button7 = tk.Button(self, text="Zarządzanie typami pojazdów", command=self.type_management)
        self.button7.pack(fill=tk.BOTH)
        self.button8 = tk.Button(self, text="Zarządzanie miejscami parkingowymi", command=self.parking_management)
        self.button8.pack(fill=tk.BOTH)
        self.button9 = tk.Button(self, text="Zarządzanie stawkami", command=self.rate_management)
        self.button9.pack(fill=tk.BOTH)
        self.button10 = tk.Button(self, text="Zarządzanie bramkami", command=self.gate_management)
        self.button10.pack(fill=tk.BOTH)
        self.button11 = tk.Button(self, text="Zarządzanie strefami", command=self.zone_management)
        self.button11.pack(fill=tk.BOTH)
        self.pack()
        self.master.resizable(False, False)

    def discount_management(self):
        newWindow = tk.Toplevel(self.master)
        app = DiscountWindow(newWindow)
        app.draw_contents()

    def type_management(self):
        # newWindow = tk.Toplevel(self.master)
        # app = TypeWindow(newWindow)
        # app.draw_contents()
        pass

    def parking_management(self):
        # newWindow = tk.Toplevel(self.master)
        # app = ParkingWindow(newWindow)
        # app.draw_contents()
        pass

    def rate_management(self):
        # newWindow = tk.Toplevel(self.master)
        # app = RateWindow(newWindow)
        # app.draw_contents()
        pass

    def gate_management(self):
        # newWindow = tk.Toplevel(self.master)
        # app = GateWindow(newWindow)
        # app.draw_contents()
        pass

    def zone_management(self):
        # newWindow = tk.Toplevel(self.master)
        # app = ZoneWindow(newWindow)
        # app.draw_contents()
        pass

    def park_zone_status(self):
        newWindow = tk.Toplevel(self.master)
        app = ParkWindow(newWindow)

    def gate_money_status(self):
        newWindow = tk.Toplevel(self.master)
        app = MoneyWindow(newWindow)

    def account_management(self):
        newWindow = tk.Toplevel(self.master)
        app = AccountWindow(newWindow)
        app.draw_contents()

    def overdraft_client_list(self):
        newWindow = tk.Toplevel(self.master)
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
        tk.messagebox.showinfo("Information", "Wygenerowano listę zaległości - plik lista.txt")


class DiscountWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Zarządzanie ulgami")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.master.geometry("320x510")
        self.grid()
        self.master.resizable(False, False)

    def draw_contents(self):
        canvas = tk.Canvas(self, width=300, height=500)
        canvas.rowconfigure(0, weight=1)
        canvas.columnconfigure(0, weight=1)
        canvas.grid(row=0, column=0, sticky="nsew")
        canvasFrame = tk.Frame(canvas)
        canvas.create_window(0, 0, window=canvasFrame, anchor='nw')
        db = MySQLdb.connect("localhost", "root", "BD2projekt!", "bd2_schema")
        cursor = db.cursor()
        sql1 = "SELECT nazwa, zniżka FROM ulgi ORDER BY id;"
        try:
            cursor.execute(sql1)
            result = cursor.fetchall()
            field_names = [i[0] for i in cursor.description]
            j = 0
            length = len(field_names)
            for j in range(length):
                label1 = tk.Label(canvasFrame, text=field_names[j], font="bold", bg="light grey")
                label1.grid(row=0, column=j, sticky="ew", padx=1, pady=1)
            button1 = tk.Button(canvasFrame, bg="tomato", text="Dodaj ulgę")
            button1.grid(row=0, column=j + 1, sticky="ew", padx=1, pady=1)
            button1.configure(command=lambda fields=field_names: self.add_discount(fields))
            for idxr, row in enumerate(result):
                idxc = 0
                for idxc, column in enumerate(row):
                    label1 = tk.Label(canvasFrame, text=column)
                    label1.grid(row=idxr + 1, column=idxc, padx=1, pady=1)
                button1 = tk.Button(canvasFrame, bg="light blue", text="Edytuj ulgę")
                button1.grid(row=idxr + 1, column=idxc + 1, sticky="ew", padx=1, pady=1)
                button1.configure(
                    command=lambda nazwa=result[idxr][0], fields=field_names: self.edit_discount(nazwa, fields))
        except:
            print("Error: Unable to fetch data")
        db.close()
        scroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        scroll.config(command=canvas.yview)
        canvas.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky="ns")
        self.update()
        canvas.configure(scrollregion=canvas.bbox("all"))

    def edit_discount(self, nazwa, field_names):
        sql1 = "SELECT nazwa, zniżka FROM ulgi WHERE nazwa = %s;"
        db = MySQLdb.connect("localhost", "root", "BD2projekt!", "bd2_schema")
        cursor = db.cursor()
        cursor.execute(sql1, nazwa)
        result = cursor.fetchone()
        newWindow = tk.Toplevel(self.master)
        app = DiscountAddWindow(result, newWindow, self)
        app.draw_contents(field_names)

    def add_discount(self, field_names):
        discdat = (None, None)
        newWindow = tk.Toplevel(self.master)
        app = DiscountAddWindow(discdat, newWindow, self)
        app.draw_contents(field_names)


class DiscountAddWindow(tk.Frame):
    def __init__(self, discdat, master=None, parent=None):
        tk.Frame.__init__(self, master)
        self.parent = parent
        self.master = master
        self.master.title("Wprowadź dane ulgi")
        self.button1 = tk.Button(self)
        self.button2 = tk.Button(self)
        self.entry1 = tk.Entry(self)
        if discdat[0] is not None:
            self.entry1.insert(0, discdat[0])
        self.entry1.configure(validate="key",
                              validatecommand=(self.register(self.on_validate_nazwa), "%d", "%i"))
        self.entry2 = tk.Entry(self)
        if discdat[1] is not None:
            self.entry2.insert(0, discdat[1])
        self.entry2.configure(validate="key",
                              validatecommand=(self.register(self.on_validate_znizka), "%d", "%P"))
        self.grid()
        self.master.resizable(False, False)

    def on_validate_nazwa(self, why, where):
        if why == '1':
            if int(where) >= 30:
                return False
        return True

    def on_validate_znizka(self, why, what):
        if why == '1':
            try:
                float(what)
            except ValueError:
                return False
        return True

    def draw_contents(self, field_names):
        length = len(field_names)
        j = 0
        for j in range(length):
            label1 = tk.Label(self, text=field_names[j])
            label1.grid(row=j, column=0, sticky="ew", padx=1, pady=1)
        label1 = tk.Label(self)
        label1.grid(row=j + 1, column=0, padx=1, pady=1)
        label1.grid(row=j + 1, column=1, padx=1, pady=1)
        self.button1 = tk.Button(self, bg="green", text="OK",
                                 command=lambda naz=self.entry1.get(): self.confirm_button_fun(naz))
        self.button1.grid(row=j + 2, column=0, sticky="ew", padx=1, pady=1)
        self.button2 = tk.Button(self, bg="tomato", text="Anuluj", command=self.master.destroy)
        self.button2.grid(row=j + 2, column=1, padx=1, pady=1)
        self.entry1.grid(row=0, column=1, sticky="ew", padx=1, pady=1)
        self.entry2.grid(row=1, column=1, sticky="ew", padx=1, pady=1)

    def confirm_button_fun(self, naz0):
        if self.entry1.get() == "" or self.entry2.get() == "":
            tk.messagebox.showerror("Error", "Pola nazwa, zniżka muszą być wypełnione")
            return
        if len(self.entry1.get()) > 30:
            tk.messagebox.showerror("Error", "Nazwa ulgi jest za długa")
            return
        if float(self.entry2.get()) >= float(100.0) or float(self.entry2.get()) <= float(0.0):
            tk.messagebox.showerror("Error", "Niepoprawna wartość zniżki (zakres 0 - 100)")
            return
        db = MySQLdb.connect("localhost", "root", "BD2projekt!", "bd2_schema")
        cursor = db.cursor()
        cursor.execute("SELECT nazwa FROM ulgi WHERE nazwa = %s;", self.entry1.get())
        naz = cursor.rowcount
        nazval = cursor.fetchone()
        if naz != 0:
            if nazval[0] != naz0:
                tk.messagebox.showerror("Error", "Istnieje już ulga o podanej nazwie")
                db.close()
                return
        sql1 = "INSERT INTO ulgi (nazwa, zniżka) VALUES (%s, %s);"
        sql2 = "UPDATE ulgi SET nazwa = %s, zniżka = %s WHERE nazwa = %s;"
        s1 = self.entry1.get()
        f1 = float(self.entry2.get())
        record = (s1, f1)
        update = (s1, f1, naz0)
        try:
            if naz0 == "":
                cursor.execute(sql1, record)
            else:
                cursor.execute(sql2, update)
        except:
            print("Error: Unable to insert data")
        db.commit()
        db.close()
        self.parent.draw_contents()
        self.master.destroy()


class TypeWindow(tk.Frame):
    def __init__(self):
        pass


class ParkingWindow(tk.Frame):
    def __init__(self):
        pass


class RateWindow(tk.Frame):
    def __init__(self):
        pass


class GateWindow(tk.Frame):
    def __init__(self):
        pass


class ZoneWindow(tk.Frame):
    def __init__(self):
        pass


class AccAddWindow(tk.Frame):
    def __init__(self, accdat, master=None, parent=None):
        tk.Frame.__init__(self, master)
        self.parent = parent
        self.master = master
        self.master.title("Wprowadź dane konta")
        self.button1 = tk.Button(self)
        self.button2 = tk.Button(self)
        self.entry1 = tk.Entry(self)
        if accdat[0] is not None:
            self.entry1.insert(0, accdat[0])
        self.entry1.configure(validate="key",
                              validatecommand=(self.register(self.on_validate_pesel), "%d", "%i", "%P"))
        self.entry2 = tk.Entry(self)
        if accdat[1] is not None:
            self.entry2.insert(0, accdat[1])
        self.entry2.configure(validate="key",
                              validatecommand=(self.register(self.on_validate_nazwisko), "%d", "%i", "%P"))
        self.entry3 = tk.Entry(self)
        if accdat[2] is not None:
            self.entry3.insert(0, accdat[2])
        self.entry3.configure(validate="key",
                              validatecommand=(self.register(self.on_validate_imie), "%d", "%i", "%P"))
        self.entry4 = tk.Entry(self)
        if accdat[3] is not None:
            self.entry4.insert(0, accdat[3])
        else:
            self.entry4.insert(0, "0.00")
        self.entry4.configure(validate="key",
                              validatecommand=(self.register(self.on_validate_saldo), "%d", "%P"))
        self.entry5 = tk.Entry(self)
        if accdat[4] is not None:
            self.entry5.insert(0, accdat[4])
        self.entry5.configure(validate="key",
                              validatecommand=(self.register(self.on_validate_telefon), "%d", "%i", "%P"))
        self.entry6 = tk.Entry(self)
        if accdat[5] is not None:
            self.entry6.insert(0, accdat[5])
        self.entry6.configure(validate="key",
                              validatecommand=(self.register(self.on_validate_email), "%d", "%i"))
        db = MySQLdb.connect("localhost", "root", "BD2projekt!", "bd2_schema")
        cursor = db.cursor()
        sql1 = "SELECT nazwa FROM ulgi;"
        try:
            cursor.execute(sql1)
            result = cursor.fetchall()
            list = [""]
            for column in result:
                list.append(column[0])
        except:
            print("Error: Unable to fetch data")
        db.close()
        self.combobox1 = ttk.Combobox(self, state="readonly", values=list)
        if accdat[6] is not None:
            self.combobox1.current(accdat[6])
        else:
            self.combobox1.current(0)
        self.entry7 = tk.Entry(self)
        if accdat[7] is not None:
            self.entry7.insert(0, accdat[7])
        self.entry7.configure(validate="key",
                              validatecommand=(self.register(self.on_validate_karta), "%d", "%i", "%P"))
        self.combobox2 = ttk.Combobox(self, state="readonly", values=["nieaktywne", "aktywne"])
        if accdat[8] is not None:
            self.combobox2.current(int(accdat[8]))
        else:
            self.combobox2.current(1)
        self.grid()
        self.master.resizable(False, False)

    def on_validate_imie(self, why, where, what):
        if why == '1':
            if int(where) < 30:
                if not what.isalpha():
                    return False
            else:
                return False
        return True

    def on_validate_nazwisko(self, why, where, what):
        if why == '1':
            if int(where) < 50:
                if not what.isalpha():
                    return False
            else:
                return False
        return True

    def on_validate_pesel(self, why, where, what):
        if why == '1':
            if int(where) < 11:
                if not what.isdigit():
                    return False
            else:
                return False
        return True

    def on_validate_saldo(self, why, what):
        if why == '1':
            try:
                float(what)
            except ValueError:
                return False
        return True

    def on_validate_telefon(self, why, where, what):
        if why == '1':
            if int(where) < 15:
                if not what.isdigit():
                    return False
            else:
                return False
        return True

    def on_validate_email(self, why, where):
        if why == '1':
            if int(where) >= 30:
                return False
        return True

    def on_validate_karta(self, why, where, what):
        if why == '1':
            if int(where) < 10:
                if not what.isalnum():
                    return False
            else:
                return False
        return True

    def draw_contents(self, field_names):
        length = len(field_names)
        j = 0
        for j in range(length):
            label1 = tk.Label(self, text=field_names[j])
            label1.grid(row=j, column=0, sticky="ew", padx=1, pady=1)
        label1 = tk.Label(self)
        label1.grid(row=j + 1, column=0, padx=1, pady=1)
        label1.grid(row=j + 1, column=1, padx=1, pady=1)
        self.button1 = tk.Button(self, bg="green", text="OK",
                                 command=lambda pes=self.entry1.get(), kod=self.entry7.get(): self.confirm_button_fun(
                                     pes, kod))
        self.button1.grid(row=j + 2, column=0, sticky="ew", padx=1, pady=1)
        self.button2 = tk.Button(self, bg="tomato", text="Anuluj", command=self.master.destroy)
        self.button2.grid(row=j + 2, column=1, padx=1, pady=1)
        self.entry1.grid(row=0, column=1, sticky="ew", padx=1, pady=1)
        self.entry2.grid(row=1, column=1, sticky="ew", padx=1, pady=1)
        self.entry3.grid(row=2, column=1, sticky="ew", padx=1, pady=1)
        self.entry4.grid(row=3, column=1, sticky="ew", padx=1, pady=1)
        self.entry5.grid(row=4, column=1, sticky="ew", padx=1, pady=1)
        self.entry6.grid(row=5, column=1, sticky="ew", padx=1, pady=1)
        self.combobox1.grid(row=6, column=1, sticky="ew", padx=1, pady=1)
        self.entry7.grid(row=7, column=1, sticky="ew", padx=1, pady=1)
        self.combobox2.grid(row=8, column=1, sticky="ew", padx=1, pady=1)

    def confirm_button_fun(self, pes0, kod0):
        if self.entry3.get() == "" or self.entry2.get() == "" or self.entry1.get() == "" or self.entry4.get() == "":
            tk.messagebox.showerror("Error", "Pola imię, nazwisko, pesel, saldo muszą być wypełnione")
            return
        if len(self.entry1.get()) != 11:
            tk.messagebox.showerror("Error", "Pesel ma niepoprawną długość")
            return
        if len(self.entry2.get()) > 50:
            tk.messagebox.showerror("Error", "Nazwisko jest za długie")
            return
        if len(self.entry3.get()) > 30:
            tk.messagebox.showerror("Error", "Imię jest za długie")
            return
        if len(self.entry5.get()) > 15:
            tk.messagebox.showerror("Error", "Numer telefonu jest za długi")
            return
        if len(self.entry6.get()) > 30:
            tk.messagebox.showerror("Error", "Email jest za długi")
            return
        if len(self.entry7.get()) > 10:
            tk.messagebox.showerror("Error", "Kod karty jest za długi")
            return
        db = MySQLdb.connect("localhost", "root", "BD2projekt!", "bd2_schema")
        cursor = db.cursor()
        cursor.execute("SELECT pesel FROM konta WHERE pesel = %s;", self.entry1.get())
        pes = cursor.rowcount
        pesval = cursor.fetchone()
        cursor.execute("SELECT kod_karty FROM konta WHERE kod_karty = %s;", self.entry7.get())
        kod = cursor.rowcount
        kodval = cursor.fetchone()
        if pes != 0:
            if pesval[0] != pes0:
                tk.messagebox.showerror("Error", "Istnieje już konto o podanym peselu")
                db.close()
                return
        if kod != 0:
            if kodval[0] != kod0:
                tk.messagebox.showerror("Error", "Istnieje już konto z podanym numerem karty")
                db.close()
                return
        sql1 = "INSERT INTO konta (imię, nazwisko, pesel, saldo, telefon, email, ulgi_id, kod_karty, aktywne) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        sql2 = "UPDATE konta SET imię = %s, nazwisko = %s, pesel = %s, saldo = %s, telefon = %s, email = %s, \
                ulgi_id = %s, kod_karty = %s, aktywne = %s WHERE pesel = %s;"
        s1 = self.entry3.get()
        s2 = self.entry2.get()
        s3 = self.entry1.get()
        f1 = float(self.entry4.get())
        if self.entry5.get() == "":
            s4 = None
        else:
            s4 = self.entry5.get()
        if self.entry6.get() == "":
            s5 = None
        else:
            s5 = self.entry6.get()
        if self.combobox1.current() == 0:
            i1 = None
        else:
            i1 = self.combobox1.current()
        if self.entry7.get() == "":
            s6 = None
        else:
            s6 = self.entry7.get()
        c1 = str(self.combobox2.current())
        record = (s1, s2, s3, f1, s4, s5, i1, s6, c1)
        update = (s1, s2, s3, f1, s4, s5, i1, s6, c1, pes0)
        try:
            if pes0 == "":
                cursor.execute(sql1, record)
            else:
                cursor.execute(sql2, update)
        except:
            print("Error: Unable to insert data")
        db.commit()
        db.close()
        self.parent.draw_contents()
        self.master.destroy()


class AccountWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Zarządzanie kontami klienckimi")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.master.geometry("970x510")
        self.grid()
        self.master.resizable(False, False)

    def draw_contents(self):
        canvas = tk.Canvas(self, width=950, height=500)
        canvas.rowconfigure(0, weight=1)
        canvas.columnconfigure(0, weight=1)
        canvas.grid(row=0, column=0, sticky="nsew")
        canvasFrame = tk.Frame(canvas)
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
                label1 = tk.Label(canvasFrame, text=field_names[j], font="bold", bg="light grey")
                label1.grid(row=0, column=j, sticky="ew", padx=1, pady=1)
            button1 = tk.Button(canvasFrame, bg="tomato", text="Dodaj konto")
            button1.grid(row=0, column=j + 1, sticky="ew", padx=1, pady=1)
            button1.configure(command=lambda fields=field_names: self.add_account(fields))
            for idxr, row in enumerate(result):
                idxc = 0
                for idxc, column in enumerate(row):
                    label1 = tk.Label(canvasFrame, text=column)
                    label1.grid(row=idxr + 1, column=idxc, padx=1, pady=1)
                button1 = tk.Button(canvasFrame, bg="light blue", text="Edytuj konto")
                button1.grid(row=idxr + 1, column=idxc + 1, sticky="ew", padx=1, pady=1)
                button1.configure(
                    command=lambda pesel=result[idxr][0], fields=field_names: self.edit_account(pesel, fields))
        except:
            print("Error: Unable to fetch data")
        db.close()
        scroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        scroll.config(command=canvas.yview)
        canvas.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky="ns")
        self.update()
        canvas.configure(scrollregion=canvas.bbox("all"))

    def edit_account(self, pesel, field_names):
        sql1 = "SELECT pesel, nazwisko, imię, saldo, telefon, email, ulgi_id, kod_karty, aktywne \
                FROM konta WHERE pesel = %s;"
        db = MySQLdb.connect("localhost", "root", "BD2projekt!", "bd2_schema")
        cursor = db.cursor()
        cursor.execute(sql1, pesel)
        result = cursor.fetchone()
        newWindow = tk.Toplevel(self.master)
        app = AccAddWindow(result, newWindow, self)
        app.draw_contents(field_names)

    def add_account(self, field_names):
        accdat = (None, None, None, None, None, None, None, None, None)
        newWindow = tk.Toplevel(self.master)
        app = AccAddWindow(accdat, newWindow, self)
        app.draw_contents(field_names)


class ParkWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Stan zapełnienia parkingów")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.master.geometry("720x510")
        self.grid()
        canvas = tk.Canvas(self, width=700, height=500)
        canvas.rowconfigure(0, weight=1)
        canvas.columnconfigure(0, weight=1)
        canvas.grid(row=0, column=0, sticky="nsew")
        canvasFrame = tk.Frame(canvas)
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
                label1 = tk.Label(canvasFrame, text=field_names[j], font="bold", bg="light grey")
                label1.grid(row=0, column=j, sticky="ew", padx=1, pady=1)
            for idxr, row in enumerate(result):
                for idxc, column in enumerate(row):
                    label1 = tk.Label(canvasFrame, text=column)
                    label1.grid(row=idxr + 1, column=idxc, padx=1, pady=1)
        except:
            print("Error: Unable to fetch data")
        db.close()
        scroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        scroll.config(command=canvas.yview)
        canvas.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky="ns")
        self.update()
        canvas.configure(scrollregion=canvas.bbox("all"))
        self.master.resizable(False, False)


class MoneyWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Stan kas bramek wyjazdowych")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.master.geometry("1220x510")
        self.grid()
        canvas = tk.Canvas(self, width=1200, height=500)
        canvas.rowconfigure(0, weight=1)
        canvas.columnconfigure(0, weight=1)
        canvas.grid(row=0, column=0, sticky="nsew")
        canvasFrame = tk.Frame(canvas)
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
                label1 = tk.Label(canvasFrame, text=field_names[j], font="bold", bg="light grey")
                label1.grid(row=0, column=j, sticky="ew", padx=1, pady=1)
            for idxr, row in enumerate(result):
                for idxc, column in enumerate(row):
                    label1 = tk.Label(canvasFrame, text=column)
                    label1.grid(row=idxr + 1, column=idxc, padx=1, pady=1)
        except:
            print("Error: Unable to fetch data")
        db.close()
        scroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        scroll.config(command=canvas.yview)
        canvas.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky="ns")
        self.update()
        canvas.configure(scrollregion=canvas.bbox("all"))
        self.master.resizable(False, False)


class OverdraftWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Lista klientów z debetem na koncie klienckim")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.master.geometry("620x510")
        self.grid()
        canvas = tk.Canvas(self, width=600, height=500)
        canvas.rowconfigure(0, weight=1)
        canvas.columnconfigure(0, weight=1)
        canvas.grid(row=0, column=0, sticky="nsew")
        canvasFrame = tk.Frame(canvas)
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
                label1 = tk.Label(canvasFrame, text=field_names[j], font="bold", bg="light grey")
                label1.grid(row=0, column=j, sticky="ew", padx=1, pady=1)
            for idxr, row in enumerate(result):
                for idxc, column in enumerate(row):
                    label1 = tk.Label(canvasFrame, text=column)
                    label1.grid(row=idxr + 1, column=idxc, padx=1, pady=1)
        except:
            print("Error: Unable to fetch data")
        db.close()
        scroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        scroll.config(command=canvas.yview)
        canvas.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky="ns")
        self.update()
        canvas.configure(scrollregion=canvas.bbox("all"))
        self.master.resizable(False, False)


def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()

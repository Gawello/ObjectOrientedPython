import pyodbc

your_user_name = "01155137@pw.edu.pl"
driver = "{ODBC Driver 18 for SQL Server}"

Driver = f"{driver};Server=tcp:gbanasik.database.windows.net,1433;Database=Projekt_BD;Uid={your_user_name};Encrypt=yes;TrustServerCertificate=no;Connection " \
         "Timeout=30;Authentication=ActiveDirectoryIntegrated"


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.connection = None

    def connect_to_database(self, server, database, username, password):
        conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        self.connection = pyodbc.connect(conn_str)

    def login(self):
        if self.connection is None:
            print("Nie połączono z bazą danych.")
            return

        name = input("Podaj imię: ")
        surname = input("Podaj nazwisko: ")

        cursor = self.connection.cursor()
        query = f"SELECT * FROM Pracownicy WHERE imie='{name}' AND nazwisko='{surname}'"
        result = cursor.execute(query).fetchone()

        if result:
            employee = Employee(self.first_name, self.last_name, self.connection)
            employee.get_status()
        else:
            print("Pracownik o podanym imieniu i nazwisku nie istnieje.")

        cursor.close()


class Employee(User):
    def __init__(self, first_name, last_name, connection):
        super().__init__(first_name, last_name)
        self.connection = connection

    def get_status(self):
        cursor = self.connection.cursor()
        query = f"SELECT Status FROM Employees WHERE Firstname='{self.first_name}' AND Lastname='{self.last_name}'"
        result = cursor.execute(query).fetchone()

        if result:
            print(f"Status pracownika {self.first_name} {self.last_name}: {result.Status}")
        else:
            print("Nie znaleziono statusu dla pracownika.")

        cursor.close()

    def create_entry(self):
        if self.connection is None:
            print("Nie połączono z bazą danych.")
            return

        entry = input("Podaj nowy wpis: ")

        cursor = self.connection.cursor()
        query = f"INSERT INTO Entries (EmployeeID, Entry) VALUES ('{self.first_name}', '{entry}')"
        cursor.execute(query)
        self.connection.commit()

        print("Nowy wpis został dodany.")
        cursor.close()

    def edit_entry(self):
        if self.connection is None:
            print("Nie połączono z bazą danych.")
            return

        entry_id = input("Podaj ID wpisu do edycji: ")
        new_entry = input("Podaj nową wartość wpisu: ")

        cursor = self.connection.cursor()
        query = f"UPDATE Entries SET Entry='{new_entry}' WHERE ID='{entry_id}'"
        cursor.execute(query)
        self.connection.commit()

        print("Wpis został zaktualizowany.")
        cursor.close()

    def delete_entry(self):
        if self.connection is None:
            print("Nie połączono z bazą danych.")
            return

        entry_id = input("Podaj ID wpisu do usunięcia: ")

        cursor = self.connection.cursor()
        query = f"DELETE FROM Entries WHERE ID='{entry_id}'"
        cursor.execute(query)
        self.connection.commit()

        print("Wpis został usunięty.")
        cursor.close


class Administrator(Employee):
    def __init__(self, first_name, last_name, connection):
        super().__init__(first_name, last_name, connection)

    def add_user(self):
        if self.connection is None:
            print("Nie połączono z bazą danych.")
            return

        new_first_name = input("Podaj nowe imię użytkownika: ")
        new_last_name = input("Podaj nowe nazwisko użytkownika: ")

        cursor = self.connection.cursor()
        query = f"INSERT INTO Employees (Firstname, Lastname) VALUES ('{new_first_name}', '{new_last_name}')"
        cursor.execute(query)
        self.connection.commit()

        print("Nowy użytkownik został dodany.")
        cursor.close()


# Przykładowe użycie programu
user = User("Gaweł", "Banasik")
user.connect_to_database(Driver)
user.login()

employee = Employee("John", "Doe", user.connection)
employee.create_entry()
employee.edit_entry()
employee.delete_entry()

administrator = Administrator("Admin", "Smith", user.connection)
administrator.add_user()

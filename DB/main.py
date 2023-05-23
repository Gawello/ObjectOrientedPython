import tkinter as tk
import pyodbc


class WindowApp(tk.Tk):
    def __init__(self, width=500, height=350):
        super().__init__()
        self.title("Logowanie")
        self.config(width=width, height=height)
        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.label_first_name = tk.Label(self, text="Imię:")
        self.label_first_name.pack()
        self.entry_first_name = tk.Entry(self)
        self.entry_first_name.pack()

        self.label_last_name = tk.Label(self, text="Nazwisko:")
        self.label_last_name.pack
        self.entry_last_name = tk.Entry(self)
        self.entry_last_name.pack()

        # Login Button
        self.login_button = tk.Button(self, text="Zaloguj", command=self.submit_login)
        self.login_button.pack()

        # Add Enter for login
        self.bind_enter_key()

    def submit_login(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()

        # Send data to database
        print("Imię: ", first_name)
        print("Nazwisko: ", last_name)

        # Clear entry
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)

    def bind_enter_key(self):
        self.login_button.focus_set()  # Set focus on login button
        self.bind("<Return>", lambda event: self.submit_login())  # Use submit login on Enter button


# Initialize login
login_window = WindowApp()
login_window.mainloop()

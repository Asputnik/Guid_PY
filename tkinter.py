import tkinter as tk

# ---------- Основной модуль
filename = "phon.txt"


class PhoneBookApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Телефонный справочник")

        self.label_1 = tk.Label(self, text="Фамилия:")
        self.label_1.grid(row=0, column=0)
        self.entry_1 = tk.Entry(self)
        self.entry_1.grid(row=0, column=1)

        self.label_2 = tk.Label(self, text="Номер телефона:")
        self.label_2.grid(row=1, column=0)
        self.entry_2 = tk.Entry(self)
        self.entry_2.grid(row=1, column=1)

        self.button_1 = tk.Button(
            self, text="Показать справочник", command=self.print_result
        )
        self.button_1.grid(row=2, column=0)
        self.button_2 = tk.Button(
            self, text="Найти по фамилии", command=self.find_by_lastname
        )
        self.button_2.grid(row=2, column=1)
        self.button_3 = tk.Button(
            self, text="Найти по номеру телефона", command=self.find_by_number
        )
        self.button_3.grid(row=3, column=0)
        self.button_4 = tk.Button(
            self, text="Добавить/изменить", command=self.add_or_change_user
        )
        self.button_4.grid(row=3, column=1)
        self.button_5 = tk.Button(self, text="Удалить", command=self.delete_by_lastname)
        self.button_5.grid(row=4, column=0)
        self.button_6 = tk.Button(self, text="Сохранить", command=self.write_txt)
        self.button_6.grid(row=4, column=1)

    def print_result(self):
        # ...
        print("Заглушка")

    def find_by_lastname(self):
        # ...
        print("Заглушка")

    def find_by_number(self):
        # ...
        print("Заглушка")

    def add_or_change_user(self):
        # ...
        print("Заглушка")

    def delete_by_lastname(self):
        # ...
        print("Заглушка")

    def write_txt(self):
        # ...
        print("Заглушка")


# ---------- Запуск ---------
app = PhoneBookApp()
app.mainloop()
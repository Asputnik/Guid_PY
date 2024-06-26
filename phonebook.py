# ---------- Основной модуль
filename_work = "phon.txt"


def work_with_phonebook():

    choice = show_menu()

    phone_book = read_txt(filename_work)

    while choice != 8:

        if choice == 1:  # "1. Отобразить весь справочник\n"
            print_result(phone_book)
        elif choice == 2:  # "2. Найти абонента по фамилии\n"
            last_name = str(input("Фамилия: "))
            print(find_by_lastname(phone_book, last_name))
            input("Press Enter to continue...")
        elif choice == 3:  # "3. Найти абонента по номеру телефона\n"
            number = input("Номер телефона: ")
            if number.isdigit():
                print(find_by_number(phone_book, number))
            else:
                print("Для поиска по номеру телефона, вводите цифры!")
            input("Press Enter to continue...")
        elif choice == 4:  # "4. Добавить абонента/изменить данные\n"
            user_data = input(
                "Введите данные через запятую, без пробелов (Фамилия,Имя,Телефон,Описание) \n"
                "[При совпадении фамилии с существующей, запись будет изменена]: "
            )  # Вопрос?
            add_or_change_user(phone_book, user_data)
            write_txt(filename_work, phone_book)
            print("Данные успешно добавлены/изменены.")
            input("Press Enter to continue...")
        elif choice == 5:  # 5. Удалить абонента по фамилии
            last_name = str(input("Фамилия: "))
            if delete_by_lastname(phone_book, last_name):
                print("Данные успешно удалены.")
            else:
                print("Данные не найдены.")
            input("Press Enter to continue...")
        elif choice == 6:  # 6. Сохранить данные в файл
            write_txt(filename_work, phone_book)
            print("Данные записаны.")
            input("Press Enter to continue...")
        elif choice == 7:  # 7. Скопировать данные в другой файл
            line_number = int(input("Введите номер строки для копирования: "))
            filename_destination = input("Введите имя файла назначения: ")
            copy_line_to_file(phone_book, line_number, filename_destination)
            print("Данные успешно скопированы.")
            input("Press Enter to continue...")
        choice = show_menu()


# ---------- Меню
def show_menu():
    print(
        "╔══════════════════════════════════════╗\n"
        "║  Телефонный справочник v.24.06.17a2  ║\n"
        "╠══════════════════════════════════════╣\n"
        "║   Выберите необходимое действие:     ║\n"
        "╠══════════════════════════════════════╣\n"
        "║ 1. Отобразить весь справочник        ║\n"
        "║ 2. Найти абонента по фамилии         ║\n"
        "║ 3. Найти абонента по номеру телефона ║\n"
        "║ 4. Добавить абонента/изменить данные ║\n"
        "║ 5. Удалить абонента по фамилии       ║\n"
        "║ 6. Сохранить данные в файл           ║\n"
        "║ 7. Скопировать данные в другой файл  ║\n"
        "║ 8. Выход (без сохранения)            ║\n"
        "╚══════════════════════════════════════╝"
    )
    while True:
        try:
            choice = int(input("Ваш выбор (1-8): "))
            if 1 <= choice <= 8:
                return choice
            else:
                choice = 0
                return choice

            #     print("Введен неправильный номер. Попробуйте снова.")
        except ValueError:
            #            print("Введен неправильный символ. Попробуйте снова.")
            choice = 0
            return choice


# ---------- Чтение файла
def read_txt(filename):
    phone_book = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename_work, "r", encoding="utf-8") as phb:
        for line in phb:
            record = dict(zip(fields, line.split(",")))
            clean_record = {key: value.strip() for key, value in record.items()}
            # dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
            # print(f"{record} , \n {clean_record}")
            # input("Жми Энтер1")
            if clean_record["Фамилия"].strip() != "":
                # filtered_record = [
                #     entry
                #     for entry in clean_record
                #     if "Фамилия" in entry
                #     and entry["Фамилия"].strip() != ""
                #     and "Телефон" in entry
                #     and entry["Телефон"].strip() != ""
                # ]
                # print(f"{record} , \n {clean_record}, \n {filtered_record}")
                phone_book.append(clean_record)
    return phone_book


# ---------- Запись файла ----------------  !!!Попробовать обьединить с Переносом записи п.7!!!
def write_txt(filename_work, phone_book):
    with open(filename_work, "w", encoding="utf-8") as phout:
        for i in range(len(phone_book)):
            s = ""
            for v in phone_book[i].values():
                s = s + v + ","
            phout.write(f"{s[:-1]}\n")


# 1 ---------- Печать справочника
def print_result(phone_book):
    if not phone_book:
        print("Справочник пуст")
        # input("Press Enter to continue...")
    else:
        print(
            "Справочник:\n"
            "═══════════════════════════════════════════════════════════════════════════════════════════"
        )

        # print("\t" "Фамилия\t" "Имя\t" "Телефон\t" "Описание")
        # for i in range(len(phone_book)):
        # print(f"{i + 1}. {list(phone_book[i].values())}")
        #    print(f"{i + 1}. {phone_book[i]}")

    # Вывод заголовка таблицы
    print(
        " ",
        "Фамилия".ljust(20),
        # "|",
        "Имя".ljust(20),
        # "|",
        "Телефон".ljust(10),
        # "|",
        "Описание".ljust(20),
        # "|",
        sep=" |",
    )
    print(
        "═══════════════════════════════════════════════════════════════════════════════════════════"
    )
    # Вывод данных
    i = 0
    for item in phone_book:
        i = i + 1
        print(
            i,
            # "|",
            item["Фамилия"].ljust(20),
            # "|",
            item["Имя"].ljust(20),
            # "|",
            item["Телефон"].ljust(10),
            # "|",
            item["Описание"].ljust(20),
            # "|",
            sep=" |",
        )
    print(
        "═══════════════════════════════════════════════════════════════════════════════════════════"
    )
    input("Press Enter to continue...")


# 2 ---------- Поиск по Фамилии
def find_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"] == last_name:
            return phone_book[i]
    return "Не найден"


# 3 ---------- Поиск по номеру телефона
def find_by_number(phone_book, number):
    for i in range(len(phone_book)):
        if phone_book[i].get("Телефон", "Нет такого номера") == number:
            #             dict.get(key[, value])Параметры get() в Python принимает максимум два параметра: key ‒ ключ для поиска в словаре; value (необязательно) ‒ значение, которое будет возвращено, если ключ не найден. Значение по умолчанию — Нет.
            # Источник: https://pythonstart.ru/dictionary/get-python
            # if phone_book[i]["Телефон"] == number:
            return phone_book[i]
    return "Не найден"


# 4 ---------- Добавить/изменить пользователя
def add_or_change_user(phone_book, user_data):
    fields = user_data.split(",")  # Собираем список
    fields = [item.strip() for item in fields]  # Убираем концевые пробелы
    print(f"\nДобавляем запись: {fields}")
    # print(*fields)
    # print(fields[2].isdigit())
    if len(fields) != 4 or not fields[2].isdigit():
        print("Неверный формат ввода данных.")
        return

    new_entry = dict(zip(["Фамилия", "Имя", "Телефон", "Описание"], fields))
    for i, entry in enumerate(phone_book):
        if entry["Фамилия"] == new_entry["Фамилия"]:  # Нашли существующую запись
            phone_book[i] = new_entry  # Заменяем данные
            return
    phone_book.append(new_entry)  # Добавляем новую запись


# 5 ---------- Удалить по фамилии
def delete_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"] == last_name:
            del phone_book[i]
            return True
    return False


# 7 ---------- Скопировать строку в другой файл ---------   !!!Попробовать обьединить с записью в файл!!!
def copy_line_to_file(phone_book, line_number, filename_destination):
    if 1 <= line_number <= len(phone_book):
        entry = phone_book[line_number - 1]
        with open(filename_destination, "a", encoding="utf-8") as file:
            file.write(
                f"{entry['Фамилия']},{entry['Имя']},{entry['Телефон']},{entry['Описание']}\n"
            )
    else:
        print("Неверный номер строки.")


# ---------- Запуск ---------
work_with_phonebook()
from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"в каком формате записать данные? \n\n"
                    f" 1 вариант:\n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 вариант:\n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: \n"))

    while var != 1 and var != 2:
        print(" Неправильный ввод")
        var = int(input('Повторите ввод! Введите 1 или 2: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name};{surname};{phone};{address}\n')

def print_data():
    print("Вывожу данные из файла 1: \n")
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))

    print("Вывожу данные из файла 2: \n")
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def search_entry():
    search_name = input("Введите имя или фамилию для поиска записи: ")
    found_entries = []
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data = f.read().strip().split("\n\n")
        for entry in data:
            if search_name in entry:
                found_entries.append(entry)

    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        for entry in data:
            if search_name in entry:
                found_entries.append(entry.strip())

    if found_entries:
        for i, entry in enumerate(found_entries):
            print(f"{i+1}. {entry}")
        return found_entries
    else:
        print("Запись не найдена.")
        return None

def edit_entry():
    entries = search_entry()
    if entries:
        index = int(input("Введите номер записи для изменения: ")) - 1
        if 0 <= index < len(entries):
            entry = entries[index]
            parts = entry.split(";") if ";" in entry else entry.split("\n")
            name = parts[0]
            surname = parts[1]
            phone = parts[2]
            address = parts[3] if len(parts) > 3 else ""

            new_name = input(f"Введите новое имя (текущее: {name}): ") or name
            new_surname = input(f"Введите новую фамилию (текущая: {surname}): ") or surname
            new_phone = input(f"Введите новый номер телефона (текущий: {phone}): ") or phone
            new_address = input(f"Введите новый адрес (текущий: {address}): ") or address

            new_entry = f"{new_name};{new_surname};{new_phone};{new_address}" if ";" in entry else f"{new_name}\n{new_surname}\n{new_phone}\n{new_address}\n\n"

            if ";" in entry:
                with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
                    data = f.readlines()
                with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
                    for line in data:
                        if line.strip() == entry:
                            f.write(new_entry + "\n")
                        else:
                            f.write(line)
            else:
                with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
                    data = f.read().strip().split("\n\n")
                with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
                    for item in data:
                        if item == entry:
                            f.write(new_entry)
                        else:
                            f.write(item + "\n\n")

            print("Запись изменена.")
        else:
            print("Некорректный номер записи.")

def delete_entry():
    entries = search_entry()
    if entries:
        index = int(input("Введите номер записи для удаления: ")) - 1
        if 0 <= index < len(entries):
            entry = entries[index]

            if ";" in entry:
                with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
                    data = f.readlines()
                with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
                    for line in data:
                        if line.strip() != entry:
                            f.write(line)
            else:
                with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
                    data = f.read().strip().split("\n\n")
                with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
                    for item in data:
                        if item != entry:
                            f.write(item + "\n\n")

            print("Запись удалена.")
        else:
            print("Некорректный номер записи.")

def main():
    while True:
        print("\nТелефонный справочник")
        print("1. Добавить запись")
        print("2. Просмотреть все записи")
        print("3. Изменить запись")
        print("4. Удалить запись")
        print("5. Выйти")
        
        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            input_data()
        elif choice == '2':
            print_data()
        elif choice == '3':
            edit_entry()
        elif choice == '4':
            delete_entry()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")



def delete_str(file="employees.csv"):
    print(f'Введите элемент имя сотрудника для удаления данных о нём из БД')
    name = input()
    lines = []

    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            if not name in line: lines += line

    with open(file, 'w', encoding="utf-8") as data:
        data.writelines(lines)




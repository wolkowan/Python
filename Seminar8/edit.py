def Edit_Entry(file="employees.csv"):
    print(f'Введите элемент имя сотрудника для изменения данных о нём в БД: ')
    name = input()
    print(f'Введите новые данные: ')
    lines = [f'{input()}\n']

    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            if not name in line: lines += line

    with open(file, 'w', encoding="utf-8") as data:
        data.writelines(lines)

    print('Изменение произведено...')

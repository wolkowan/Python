def New_Entry():
    ID = input('Введите ID: ')
    sirname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    father_name = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    department = input('Введите отдел: ')
    position = input('Введите должность: ')
    with open('employees.csv','a', encoding='utf-8') as book:
        book.write(f'{ID}, {sirname}, {name}, {father_name}, {phone}, {department}, {position};\n')

def reading():
    contacts = [0] * 4
    contacts[0] = input("Введите фамилию: ")
    contacts[1] = input("Введите имя: ")
    contacts[2] = input("Введите Телефон: ")
    contacts[3] = input("Введите описание: ")
    return contacts

def newstring(contacts):
    bazaopen = open("BAZA.txt", "a", encoding = 'utf-8')
    bazaopen.write(contacts + '\n')
    bazaopen.close()



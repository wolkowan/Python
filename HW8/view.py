def startMenu():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print('Выберите действие: ')
    print(f"""
    1: Создание справочника студентов и внесение первой записи;
    2: Добавление новой записи в существующий справочник студентов;
    3: Вывод всего справочника;
    4: Вывести полные данные об объекте;
    5: Вывод определенной выборки;
    
    8: Выход из программы.
    
    Ваш выбор:

    """)
    print()
    operators = input()
    return operators

def view_info():
    print("""
    По какому атрибуту будет осуществляться поиск:
    1. По id;
    2. По фамилии;
    3. По городу;
    4. По статусу
    
    """)
    choice=input()
    return choice


def ask_id():
    id=input("Введите id: ")
    return id
def ask_status():
    id=input("Введите статус: ")
    return id
def ask_town():
    id=input("Введите город проживания: ")
    return id



def ask_first_name():
    name=input("Внесите имя:")
    return name

def ask_second_name():
    name=input("Внесите отчество:")
    return name

def ask_last_name():
    name=input("Внесите фамилию:")
    return name

def print_row(row):
    print(row)
def printAll():
    with open("csv_ex_1", 'r', encoding="utf-8") as file:
        print("Загрузка данных из файла 'csv_ex_1'")
        print(file.read())
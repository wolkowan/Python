import model

def startMenu():
    print('Выберите действие: ')
    print(f"1: Внести новую запись в телефонную книгу;\n2: Вывод всего справочника;\n3: Загрузка базы данных из внешнего источника;\n4: Выход из программы.")
    print()
    operators = input()
    return operators

def inputNote():

    name = input('Введите имя')
    surname = input('Введите фамилию')
    number = input('Введите номер телефона')
    info= input('Введите дополнительную информацию')
    model.newNoteCSV(name, surname, number, info)
    model.newNoteHTML(name, surname, number, info)
    model.newNoteMD(name, surname, number, info)
    model.newNoteTXT(name, surname, number, info)



def AskFormatForPrintFile():
    print("Выберете формат файла для вывода данных.\n1. csv;\n2. md;\n3. html;\n4. txt")
    fileFormat = int(input())
    return fileFormat

def printAllTxt():
    with open('phonebook.txt', 'r', encoding="utf-8") as file:
        print("Загрузка данных из файла phonebook.txt")
        print(file.read())
def printAllCSV():
    with open('phonebook.csv', 'r', encoding="utf-8") as file:
        print("Загрузка данных из файла phonebook.csv")
        print(file.read())

def printAllMd():
    with open('phonebook.md', 'r', encoding="utf-8") as file:
        print("Загрузка данных из файла phonebook.md")
        print(file.read())

def printAllHtml():
    with open('phonebook.html', 'r') as file:
        print("Загрузка данных из файла phonebook.html")
        print(file.read())

# def inputPath():
#     path = input("Введите путь для скачивания данных")
#     return path



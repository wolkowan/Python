import model


def inputNote():
    name= input('Введите имя')
    surname= input('Введите фамилию')
    number=input('Введите номер телефона')
    model.newNoteCSV(name,surname,number)
    model.newNoteHTML(name, surname, number)
    model.newNoteMD(name, surname, number)
    model.newNoteTXT(name, surname, number)

def printAll():
    with open('phonebook.txt', 'r', encoding="utf-8") as file:
        print(file.read())
import view





def start():
    print('Выберите действие: ')
    print(f"1: Внести новую запись в телефонную книгу;\n2: Вывод всего справочника;\n3:Выход из программы.")
    print(":")

    operators = int(input())
    if operators==1:
        result= view.inputNote()
        return result
    elif operators==2:

        result= view.printAll()
        return result
    elif operators==3:
        print("Выход")







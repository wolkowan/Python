
def a1():
    # Ваша программа должна считать одно натуральное число, после чего вывести:
    #
    # “Fizz”, если это число делится на 3;
    # “Buzz”, если это число делится на 5;
    # “FizzBuzz”, если выполнены оба предыдущих условия;
    # само это число в остальных случаях.
    a= int(input())
    if a%3==0 and a%5!=0:
        print("Fizz")
    elif a%5==0 and a%3!=0:
        print("Buzz")
    elif a%3==0 and a%5==0:
        print('FizzBuzz')
    else:
        print(a)

# Программа определяет наименование месяца по его номеру n. Название месяца пишется с заглавной буквы
#
# Программа получает на вход номер месяца - натуральное число N (N<=12) и в зависимости от его значения вывод название месяца
def a2():


    N= int(input())
    if N==1:
        print("Январь")
    elif N==2:
        print("Февраль")
    elif N==3:
        print("Март")
    elif N==4:
        print("Апрель")
    elif N==5:
        print("Май")
    elif N==6:
        print("Июнь")
    elif N==7:
        print("Июль")
    elif N==8:
        print('Август')
    elif N==9:
        print('Сентябрь')
    elif N==10:
        print('Октябрь')
    elif N==11:
        print('Ноябрь')
    elif N==12:
        print('Декабрь')

a2()

def case():
    n = int(input())
    match n:
        case 1:
            print("Совсем еще зеленый студентик")
        case 2:
            print("Джун-студент")
        case 3:
            print("Мидл-студент")
        case 4:
            print("Сеньер-студент")
        case 5:
            print("Босс качалки")
        case _:
            print("Неизвестный курс")










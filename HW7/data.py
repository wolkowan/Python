import random
import csv
import logger as lg


file = open('base_phone.csv', 'w')
newrecord = "ID,Name,Surname,PhoneNumber\n"
file.writelines(newrecord)

ls_name = ['Svetlana', 'Olga', 'Anton', 'Anna', 'Inna',
           'Viktor', 'Vasilisa', 'Alex', 'Miron', 'Igor', 'Anna']
ls_surname = ['Kovalenko', 'Sidorenko', 'Mironenko',
              'Galich', 'Shapiro', 'Duma', 'Duma', 'Shagal', 'Moroz']



def list_of_numbers():

    randomListPhone = random.randint(79000000000, 80000000000)
    # s = s + str(randomListPhone)

# рандомно соеденить имена фамилии и номера телефонов (отдельный метод) def + присвоение id


def string_creation():
    s = ""
    s = s + random.choice(ls_name) + ',' + random.choice(ls_surname) + ',' + \
        list_of_numbers()
    return s


def start():
    for i in range(100):
        a = f'{str(i + 1)},{string_creation()}\n'
        file.write(a)
    file.close()


start()
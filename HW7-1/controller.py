import csv
import os.path
import logger as lg


db_file_name = ''
db = []
global_id = 0


def init_data_base(file_name='db.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name

    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    if(int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()


def create(name='', surname='', number=''):
    global global_id
    global db
    global db_file_name
    if(name == ''):
        print("Не указано имя")
        return
    if(surname == ''):
        print("Не указана фамилия")
        return
    if(number == ''):
        print("Не указан номер телефона")
        return

    for row in db:
        if(row[1] == name and row[2] == surname and row[3] == number):
            print("Уже есть в книге")
            return

    global_id += 1
    new_row = [str(global_id), name,
               surname, number]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


# поиск и выгрузка данных по запросу
def retrive(id='', name='', surname='', number=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(name != '' and row[1] != name):
            continue
        if(surname != '' and row[2] != surname):
            continue
        if(number != '' and row[3] != number):
            continue

        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:

        return result


def update(id='', new_name='', new_surname='', new_number=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('Укажите ID')
        return
    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if(row[0] == id):
                if(new_name != ''):
                    row[1] = new_name

                if(new_surname != ''):
                    row[2] = new_surname

                if(new_number != ''):
                    row[3] = new_number

            writer.writerow(row)


def delete(id=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('Укажите ID')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)


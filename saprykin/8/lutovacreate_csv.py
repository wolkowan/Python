import csv


def create_base():

    with open("csv_ex_1", 'w', encoding='utf-8') as csvfile:
        fname=['id', 'first_name','second_name', "last_name"]
        csv_writer= csv.DictWriter(csvfile, fieldnames=fname)
        csv_writer.writeheader()

        for i in range(1,11):
            csv_writer.writerow(
                { 'id': i, 'first_name':f'Имя_{i}', 'second_name':f'Отчество_{i}', "last_name":f'Фамилия_{i}' })

def max_id():
    with open("csv_ex_1", 'r', encoding='utf-8') as csvfile:
        reader= csv.DictReader(csvfile)
        max_id=1
        for row in reader:
            if max_id<int(row['id']):
                max_id= int(row['id'])
        return max_id


def add():
    with open("csv_ex_1", 'a', encoding='utf-8') as csvfile:
        fname = ['id', 'first_name', 'second_name', "last_name"]
        csv_writer = csv.DictWriter(csvfile, fieldnames=fname)
        csv_writer.writerow({
            'id': max_id()+1,

            'first_name': 'Иван',
            'second_name': 'Иванович',
            "last_name" : "Иванов"

        })


add()


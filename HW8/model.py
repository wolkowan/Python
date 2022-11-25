import csv
import view


def create_base():


        with open("csv_ex_1", 'w', encoding='utf-8') as csvfile:
            fname=['id', 'first_name','second_name', "last_name","status", "town"]
            csv_writer= csv.DictWriter(csvfile, fieldnames=fname)
            csv_writer.writeheader()

            # for i in range(1,2):
            #     csv_writer.writerow(
            #         { 'id': i, 'first_name':f'Имя_{i}', 'second_name':f'Отчество_{i}', "last_name":f'Фамилия_{i}' })




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
        fname = ['id', 'first_name', 'second_name', "last_name","status", "town"]
        csv_writer = csv.DictWriter(csvfile, fieldnames=fname)
        csv_writer.writerow({
            'id': max_id()+1,

            'first_name': view.ask_first_name(),
            'second_name': view.ask_second_name(),
            "last_name" : view.ask_last_name(),
            "status":view.ask_status(),
            "town":view.ask_town()


        })

def first_add():
    with open("csv_ex_1", 'a', encoding='utf-8') as csvfile:
        fname = ['id', 'first_name', 'second_name', "last_name","status", "town"]
        csv_writer = csv.DictWriter(csvfile, fieldnames=fname)
        csv_writer.writerow({
            'id': 1,

            'first_name': view.ask_first_name(),
            'second_name': view.ask_second_name(),
            "last_name" : view.ask_last_name(),
            "status": view.ask_status(),
            "town": view.ask_town()

        })

def find_by_id():
    try:
        with open("csv_ex_1", 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            id=view.ask_id()
            for row in reader:
                for i in row:
                    if row[i]==id:
                        return (row)

    except Exception:
       print('ID не существует')

def find_by_last_name():

    with open("csv_ex_1", 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)


        name=view.ask_status()



        for row in reader:

                if row['last_name']==name:
                    return (row)



def find_status():

    with open("csv_ex_1", 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        result = []
        status=view.ask_status()
        for row in reader:

                if row['status']== status:
                    result.append(row)
                    result.append("\n")

        return result

def find_town():

    with open("csv_ex_1", 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        result = []
        town=view.ask_town()
        for row in reader:

                if row['town']== town:
                    result.append(row)
        return result
















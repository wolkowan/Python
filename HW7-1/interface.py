import controller as cr
import logger as lg


def ls_menu():

    while True:
        print('\nМЕНЮ')
        print('1. Показать все записи.')
        print('2. Найти номер по фамилии.')
        print('3. Найти номер по имени.')
        print('4. Поиск по номеру телефона.')
        print('5. Добавить новую запись.')
        print('6. Изменить существующую запись.')
        print('7. Удалить запись.')
        print('8. Закрыть программу.\n')
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 1:
            lg.logger('The user has selected item number 1')

            print(cr.retrive())

        elif n == 2:
            lg.logger('The user has selected item number 2')
            search = input('Введите фамилию: ')
            lg.logger(f'User entered: {search}')
            print(cr.retrive(surname=search))

        elif n == 3:
            lg.logger('The user has selected item number 3')
            search = input('Введите имя: ')
            lg.logger(f'User entered: {search}')
            print(cr.retrive(name=search))

        elif n == 4:
            lg.logger('The user has selected item number 4')
            search = input('Введите номер  телефона: ')
            lg.logger(f'User entered: {search}')
            print(cr.retrive(number=search))

        elif n == 5:
            lg.logger('The user has selected item number 5')
            name = input('Введите имя: ')
            lg.logger(f'User entered: {name}')
            surname = input('Введите фамилию: ')
            lg.logger(f'User entered: {surname}')
            number = input('Введите номер телефона: ')
            lg.logger(f'User entered: {number}')

            cr.create(name, surname, number)

        elif n == 6:
            lg.logger('The user has selected item number 6')
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            change = сhecking_the_number(input('Введите номер пункта: '))

            if change == 1:
                lg.logger('The user has selected item number 6.1')
                search = input('Введите фамилию: ')
                lg.logger(f'User entered: {search}')
                cr.retrive(surname=search)
                user_id = input('Введите id записи: ')
                lg.logger(f'User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                lg.logger(f'User entered: {new_number}')
                cr.update(id=user_id, new_number=new_number)

            elif change == 2:
                lg.logger('The user has selected item number 6.2')
                search = input('Введите имя: ')
                lg.logger(f'User entered: {search}')
                cr.retrive(name=search)
                user_id = input('Введите id записи: ')
                lg.logger(f'User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                lg.logger(f'User entered: {new_number}')
                cr.update(id=user_id, new_number=new_number)

            elif change == 3:
                lg.logger('The user has selected item number 6.3')
                search = input('Введите номер телефона: ')
                lg.logger(f'User entered: {search}')
                cr.retrive(number=search)
                user_id = input(f'Введите id записи: ')
                lg.logger(f'User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                lg.logger(f'User entered: {new_number}')
                cr.update(id=user_id, new_number=new_number)

            else:
                lg.logger('User entered an invalid menu value')
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 7:
            lg.logger('The user has selected item number 7')
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            deleting = сhecking_the_number(input('Введите номер пункта: '))

            if deleting == 1:
                lg.logger('The user has selected item number 7.1')
                search = input('Введите фамилию: ')
                lg.logger(f'User entered: {search}')
                print(cr.retrive(surname=search))
                user_id = input('Введите id записи: ')
                lg.logger(f'User entered: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 2:
                lg.logger('The user has selected item number 7.2')
                search = input('Введите имя: ')
                lg.logger(f'User entered: {search}')
                print(cr.retrive(name=search))
                user_id = input('Введите id записи: ')
                lg.logger(f'User entered: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 3:
                lg.logger('The user has selected item number 7.3')
                search = input('Введите номер телефона: ')
                lg.logger(f'User entered: {search}')
                print(cr.retrive(number=search))
                user_id = input('Введите id записи: ')
                lg.logger(f'User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                cr.delete(id=user_id)

            else:
                lg.logger('User entered an invalid menu value')
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 8:
            lg.logger('End')
            print('Выход из программы')
            break

        else:
            lg.logger('User entered an invalid menu value: {n}')
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')




def сhecking_the_number(arg):
    while arg.isdigit() != True:
        lg.logger('User entered an invalid menu value: {arg}')
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)

import random

numb_type = 'r'
numb_value = 0
numb_oper = '+'


def get_type(chck=''):
    global numb_type

    chck = True
    while (chck):
        chck = True
        numb_type = input('введите тип числа (r - real, c - complex): ')
        if numb_type in ('r', 'c'): chck = False

    return numb_type


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_frac(value):
    st = value.split('/')
    if len(st) != 2: return False
    if st[0].replace(' ', '0').replace('-', '0').isdigit() and st[1].replace(' ', '0').isdigit():
        return True
    else:
        return False


def is_complex(value):
    try:
        complex(value)
        if complex(value).imag == 0:
            return False
        else:
            return True
    except ValueError:
        return False


def rc():
    return random.choice([-1, 1])


def get_value(flag):
    global numb_value
    if flag == 0:
        chck = True
        while (chck):
            chck = True
            if numb_type == 'r':
                numb_value = input('''Формат вещественных чисел с использованием "." (пример, 9.48); 
                в виде дроби в формате "[целое часть] пробел [числитель] / [знаменатель] (пример, 2 3/5).
                Введите число:   ''')
                if is_float(numb_value) or is_frac(numb_value):
                    chck = False
                else:
                    print('Не вещественное число')
            if numb_type == 'c':
                numb_value = input(
                    'Формат комплексных чисел: [действительная часть] + [мнимая часть]j (пример, 2-3j).  Введите число:')
                if is_complex(numb_value):
                    chck = False
                else:
                    print('Не комплексное число')
    elif flag == 1:
        if rd == 0:
            numb_value = str(random.uniform(-10, 10))
        else:
            numb_value = f'{rc() * random.randint(1, 10)} {random.randint(1, 9)}/{random.randint(1, 9)}'
    elif flag == 2:
        numb_value = str(complex(rc() * random.randint(1, 10), rc() * random.randint(1, 10)))[1:-1]
    return numb_value


def get_oper(chck):
    global numb_oper
    op = ['+', '-', '*', '/']

    chck = True
    while (chck):
        numb_oper = input('введите оператор (+, -, * or /): ')
        if numb_oper in op: chck = False
    return numb_oper


def view_res(flag, res):
    if flag == 0:
        chck = True
        while (chck):
            chck = True
            res_path = input('вывод результата (c - консоль, f - файл): ')
            if res_path in ('c', 'f'): chck = False
    else:
        res_path = 'f'
    if res_path == 'c':
        print(res)
    else:
        with open('res.txt', 'a') as rs:
            rs.write(f'{res}\n')
    return res


def menu_collection(ch):
    get_type(ch)
    return (get_value(ch), get_value(ch), get_oper(ch))
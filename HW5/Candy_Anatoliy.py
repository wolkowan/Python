print(f'\n____2. Игра с конфетами____\n')

import random

import random

def Enter_number(text = '', type = 2): # функция ввода числа с проверкой
    print(text)
    while True:
        if type == 1:
            try:
                value = int(input())
                break
            except:
                print("Ошибка! Введите целое число:")
        elif type == 2 or type == 3:
            try:
                if type == 2:
                    value = float(input())
                    break
                elif type == 3:
                    from decimal import Decimal
                    value = Decimal(input())
                    break
            except:
                print("Ошибка! Введите число:")
    return value

def Candies_game(candies=2021, candies_max=28, game_type=1):
    move = random.randint(1, 2)
    round = 1
    candies_given = 0

    print(
        f'На столе лежат конфеты. Игроки 1 и 2 ходят по очереди. За один ход можно забрать не более чем {candies_max} конфет.')
    print(f'Все конфеты оппонента достаются сделавшему последний ход.\nПервый ход делает {move} игрок')

    if game_type == 1:
        print('\nРежим игры "Игрок против игрока"')

        while candies != 0:
            print(f'\nРаунд {round}. Конфет на столе - {candies} шт.')

            if candies < candies_max: candies_max = candies

            print(f'Ход игрока {move}. Возьмите не более {candies_max} шт. конфет: ', end='')

            while True:
                candies_given = Enter_number()
                if 1 <= candies_given <= candies_max:
                    break
                else:
                    print(f'Введите число от 1 до {candies_max}: ', end='')

            candies -= candies_given

            if candies == 0:
                print(f'\nИгрок {move} победил!!! Все конфеты Ваши!')
                break

            round += 1

            if move == 1:
                move = 2
            else:
                move = 1

    if game_type == 2 or game_type == 3:
        if game_type == 2:
            print('\nРежим игры "Игрок против компьютера (упрощённый вариант)"')
        elif game_type == 3:
            print('\nРежим игры "Игрок против компьютера (интеллектуальный бот)"')

        if move == 1:
            while candies != 0:
                print(f'\nРаунд {round}. Конфет на столе - {candies} шт.')

                if candies < candies_max: candies_max = candies

                print(f'Ваш ход. Возьмите не более {candies_max} шт. конфет: ', end='')

                while True:
                    candies_given = Enter_number()
                    if 1 <= candies_given <= candies_max:
                        break
                    else:
                        print(f'Введите число от 1 до {candies_max}: ', end='')

                candies -= candies_given

                if candies == 0:
                    print(f'\nВы победили!!! Все конфеты Ваши!')
                    break

                if candies < candies_max: candies_max = candies

                print(f'Ход компьютера. Нажмите "enter" для продолжения...', end='')
                input()

                if game_type == 2:
                    candies_bot = random.randint(1, candies_max)
                    candies -= candies_bot
                elif game_type == 3:
                    candies_bot = candies % (candies_max + 1)
                    if candies_bot == 0: candies_bot = random.randint(1, candies_max)
                    candies -= candies_bot

                if candies == 0:
                    print(f'\nПоражение! Компьютер взял {candies_bot} шт. конфет и победил. Все конфеты достаются ему.')
                    break
                else:
                    print(f'Компьютер взял {candies_bot} шт. конфет. Осталось {candies}')

                round += 1

                if move == 1:
                    move = 2
                else:
                    move = 1

        if move == 2:
            while candies != 0:
                print(f'\nРаунд {round}. Конфет на столе - {candies} шт.')

                if candies < candies_max: candies_max = candies

                print(f'Ход компьютера. Нажмите "enter" для продолжения...', end='')
                input()

                if game_type == 2:
                    candies_bot = random.randint(1, candies_max)
                    candies -= candies_bot
                elif game_type == 3:
                    candies_bot = candies % (candies_max + 1)
                    if candies_bot == 0: candies_bot = random.randint(1, candies_max)
                    candies -= candies_bot

                if candies == 0:
                    print(f'\nПоражение! Компьютер взял {candies_bot} шт. конфет и победил. Все конфеты достаются ему.')
                    break
                else:
                    print(f'Компьютер взял {candies_bot} шт. конфет. Осталось {candies}')

                if candies < candies_max: candies_max = candies

                print(f'Ваш ход. Возьмите не более {candies_max} шт. конфет: ', end='')

                while True:
                    candies_given = Enter_number()
                    if 1 <= candies_given <= candies_max:
                        break
                    else:
                        print(f'Введите число от 1 до {candies_max}: ', end='')

                candies -= candies_given

                if candies == 0:
                    print(f'\nВы победили!!! Все конфеты Ваши!')
                    break

                round += 1

                if move == 1:
                    move = 2
                else:
                    move = 1


candies_num = random.randint(50, 100)
maximum = random.randint(5, 30)

Candies_game(candies=candies_num, candies_max=maximum, game_type=3)

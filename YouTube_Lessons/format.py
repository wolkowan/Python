# name = 'Семён'
# mid_name = 'Семёнов'
# balance = 32.56
#
# text = """Дорогой {0} {1},
# баланс Вашего лицевого счёта составляет {2} руб.""".format(name, mid_name, balance)
#
# print(text)
#
#
# name = 'Семён'
# mid_name = 'Семёнов'
# balance = 32.56
#
# text = """Дорогой {n} {m},
# баланс Вашего лицевого счёта составляет {b} руб.""".format(m=mid_name, n=name, b=balance)
#
# print(text)
#
#
# num= int(input())
# num1=num-1
# num2=num+1
# print('''
# Для числа {0} предыдущим будет число {1}.
# Для числа {0} следующим будет число {2}.'''.format(num,num1,num2))
#
#
# n = 123456789123
#
# print(f'{n:,d}')
# print(f'{n:_d}')
# print(f'{n:.2f}')
#
# sep = '_'
# print(f'{n:{sep}d}') # вложенная f-строка
#
# n=int(input())
# print(f'{n:010n}')

# number = 12345.6789
# print(f"Число {number = }")
# print(f"|{number:25}|")
# print(f"|{number:<25}|")
# print(f"|{number:>25}|")
# print(f"|{number:^25}|")
# print('-'*25)
# text = "Python 3.10"
# print(f"Строка {text = }")
# print(f"|{text:25}|")
# print(f"|{text:<25}|")
# print(f"|{text:>25}|")
# print(f"|{text:^25}|")


APPLES = .50
BREAD = 1.50
CHEESE = 2.25
num_apples = 3
num_bread = 10
num_cheese = 6
price_apples = num_apples * APPLES
price_bread = num_bread * BREAD
price_cheese = num_cheese * CHEESE
str_apples = 'Яблоки'
str_bread = 'Хлеб'
str_cheese = 'Сыр'
total = price_bread*num_bread + price_cheese*num_cheese + price_apples*num_apples
print(f'{"Список покупок":^30s}')
print(f'{"=" * 30}')
print(f'{str_apples:10s}{num_apples:10d}\t${price_apples:>5.2f}')
print(f'{str_bread:10s}{num_bread:10d}\t${price_bread:>5.2f}')
print(f'{str_cheese:10s}{num_cheese:10d}\t${price_cheese:>5.2f}')
print(f'{"Total:":>20s}\t${total:>5.2f}')


text = input()
print(f"|{text:&^20}|")
print(f"|{text:&>20}|")
print(f"|{text:&<20}|")
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#  Пример:
# 6782 -> 23
# 0,56 -> 11

a= input("Вещественное число: ")

b = list(map(int, filter(lambda x: x not in ('-', '.', ','), a)))

print(sum(b))

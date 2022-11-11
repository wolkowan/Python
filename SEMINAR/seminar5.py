# import math
# n = int(input('Введите количество цифр после запятой: '))
# print('Число 𝜋: {:.50f}'.format(math.pi))
# a = math.pi
# b = round(a,n+1)*10**n
# c = math.modf(b)
# a = c[1] / 10**n
# print(f'Число 𝜋 с заданной точностью:  {a:.50f}  ')
#
#
# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#
#  Пример:
#
#  2+2 => 4;
#
#  1+2*3 => 7;
#
#  1-2*3 => -5;
#
#
# Добавьте возможность использования скобок, меняющих приоритет операций.
#
#  Пример:
#
#  1+2*3 => 7;
#
#  (1+2)*3 => 9;


# s= '1+(2+14)/(4-2)'
# print(eval(s))
#
# import re
#
# actions = {
#  "^": lambda x, y: str(float(x) ** float(y)),
#  "*": lambda x, y: str(float(x) * float(y)),
#  "/": lambda x, y: str(float(x) / float(y)),
#  "+": lambda x, y: str(float(x) + float(y)),
#  "-": lambda x, y: str(float(x) - float(y))
# }
#
# priority_reg_exp = r"\((.+?)\)"
# action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
#
#
# def my_eval(expresion: str) -> str:
#  while (match := re.search(priority_reg_exp, expresion)):
#   expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))
#
#  for symbol, action in actions.items():
#   while (match := re.search(action_reg_exp.format(symbol), expresion)):
#    expresion: str = expresion.replace(match.group(0), action(*match.groups()))
#
#  return expresion

#
# exp = "(1 + 4) * (5 * (10 - 2)) / 5"
# print(my_eval(exp), eval(exp))  # 40.0 40.0
#
# import random
#
# random_list = [random.randint(1, 20) for i in range(random.randint(10, 30))]
# print(random_list)
# print(list(set(random_list)))
# uniq_list = [i for i in set(random_list) if random_list.count(i) == 1]
# print(uniq_list)




formula = '24/2*3+30'
lst = []
for i in formula:
    if i.isdigit():
        numbers+=i
    else:
        lst.append(numbers)
        numbers=''
        lst.append(i)
lst.append(numbers)
print(lst)

i = 0
while '/' in lst or '*' in lst:
    if lst[i] == '/':
        print(Action(lst,'/'))
        i = 0
    elif lst[i] == '*':
        print(Action(lst,'*'))
        i = 0
    else:
        i+=1

i = 0
while '-' in lst or '+' in lst:
    if lst[i] == '-':
        print(Action(lst,'-'))
        i = 0
    elif lst[i] == '+':
        print(Action(lst,'+'))
        i = 0
    else:
        i+=1
print(lst)


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


s=[1.1, 1.2, 3.1, 5, 10.01]

min= float((s[0]))%1
max= float((s[0]))%1

for i in s:
    i=(float(i)%1)
    if i==0:
        continue
    if i>max:
        max=i
    elif i<min:
        min=i

print(f'Mинимальное значение дробной части элементов {round(min, 4)}')
print(f'Mаксимальное значение дробной части элементов {round(max, 4)}')
print(f'Разницa между максимальным и минимальным значением дробной части элементов {round((max-min),4)}')


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#  Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# В решении реализовано два варианта вывода, на экран и для записи в файл (из-за невозможности (незнании способа) записи в файл в кодировке UTF-8).

# ПРОШУ РАЗОБРАТЬ ВОПРОС КОДИРОВОК НА СЕМИНАРЕ

import random

k = int(input("Задайте натуральную степень К от 1 до 9: "))

ind = []
for i in range(k+1):
    ind.append(random.randint(0, 3))
print(f'Сформировынный случайным образом список коэффициентов:  {ind}')


s_to_file = ''

for i in range(len(ind)-1):
    if ind[i] != 0:
        if (k-i) == 1:

            s_to_file += str(ind[i])+"x + "
        else:

            s_to_file += str(ind[i])+"x^" + str(k-i)+' + '


itog_to_file = s_to_file + str(ind[-1])+" = 0"
print(itog_to_file)
print("Результат сохранен в файл file_HW4.txt")



with open('file.txt', 'w', encoding = "utf-8") as file:
    file.write('текст')


file = open("file_HW4.txt", 'a')
file.write(itog_to_file)
file.write('\n')

file.close()

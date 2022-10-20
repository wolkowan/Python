
import random

dict = {
    0: "\u2070",
    1: "\u00B9",
    2: "\u00B2",
    3: "\u00B3",
    4: "\u2074",
    5: "\u2075",
    6: "\u2076",
    7: "\u2077",
    8: "\u2078",
    9: "\u2079"
}

k = int(input("Задайте натуральную степень К от 1 до 9: "))

ind = []
for i in range(k+1):
    ind.append(random.randint(0, 101))
print(f'Сформировынный случайным образом список коэффициентов:  {ind}')


s = ''
for i in range(len(ind)-1):
    if ind[i] != 0:
        if (k-i) == 1:
            s += str(ind[i])+"x + "
        else:
            s += str(ind[i])+"x" + dict[k-i]+' + '

itog = s+str(ind[-1])+" = 0"
print(itog)

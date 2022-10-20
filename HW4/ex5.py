# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.

# Задача реализована с ограничениями: количество членов в многочленax должно быть одинаковым,
# переменная одна и обозначена "х", степень х - натуральное число в диапазоне от 0 до 9. Количество складываемых многочленов- 2.


f = open("file_HW4_1.txt", encoding="utf-8")
s1 = f.read()
print(f'Превый многочлен: {s1}')
f.close()

f = open("file_HW4_2.txt", encoding="utf-8")
s2 = f.read()
print(f'Второй  многочлен: {s2}')
f.close()

s1 = list((s1).split(" + "))
s2 = list((s2).split(" + "))


s3 = []
for i in s2:
    if "^" in i:
        for j in s1:
            if "^" in j:
                if i[-1] == j[-1]:
                    koef = str((int(i[:-3])+int(j[:-3])))
                    s3.append(koef + i[-3:])

    elif 'x' in i:
        for j in s1:
            if "x" in j and "^" not in j:
                koef = str((int(i[:-1])+int(j[:-1])))
                s3.append(koef + i[-1:])
    else:
        for j in s1:
            if "x" not in j and "^" not in j:
                koef = str(int(i)+int(j))
                s3.append(koef)
s3 = '+'.join(s3)


print(f'Сумма многочленов  равна {s3}')
print("Результат сохранен в файл file_HW4_3.txt")

file = open('file_HW4_3.txt', 'w')
file.write(s3)
file.close()

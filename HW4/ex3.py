# 3. Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.
#(10 10 10 10 20------->10 20)
# a = input("Задайте последовательность: ").split()
# s = set()
# for i in a:
#     s.add(i)
# print(list(s))


b = input("Задайте последовательность: ").split()
c=[]

for i in b:
    if i not in c:
        c.append(i)
print(c)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.  (10,10,10,20---->20)

s= list(map(int, input("введите последовательность через пробел").split()))
s1=[i for i in s if s.count(i)==1]
print(s1)
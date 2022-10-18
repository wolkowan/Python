#Генератор списков

z=[i**2 for i in range(7)]
print(z)

b=[i*2 for i in "hello"]
print(b)

import random
c=[random.randint(-10,10) for i in range(10)]
d=[abs(i) for i in c]
print(c)
print(d)

# e=input("print num: ").split()
# e=[int(i) for i in e]
# print(e)


#создаем двумерный массив mxn

n=3
m=4

a = [[0] * m for i in range(n)]
for i in a:
    print(i)

g = [i * j for i in [2, 3, 4, 5] for j in [1, 2, 3] if i * j >= 10]
print(g)

h = [(i, j) for i in "abc" for j in  [1, 2, 3]]
print(h)

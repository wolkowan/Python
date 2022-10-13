#5. Реализуйте алгоритм перемешивания списка.
s= [1,3,5,6,8,9,10]
import random
# # Вариант решения
# random.shuffle(s)
# print(s)

for i in range(0,len(s)):
    j = random.randint(0, len(s))
    s[i], s[j] = s[j], s[i]
     
print (s)

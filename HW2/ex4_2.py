import random
N=int(input("Задайте количество элементов в списке:"))

file = open("file2.txt", 'w')
file.write(str(random.randint(0, N+1)))
file.write('\n')
file.writelines(str(random.randint(0, N+1)))
file.write('\n')
file.writelines(str(random.randint(0, N+1)))
file.write('\n')
file.close()



#Создаю список случайных элементов:
s=[]
for i in range(1, N+1):
    s.append(random.randint(-N, N))
print(f'Cписок из {N} элементов, заполненных числами из промежутка [{-N}, {N}] : {s}')
print()

#Открываю файл в режиме чтения, получаю номера позиций элементов, вычисляю произведение элементов
file=open('file2.txt', 'r')
product=1
print('Содержание файла:')
for i in file:
    print(i, end='')
    if int(i) < len(s):
        product*=s[int(i)]
    
file.close()
print()
print(f'Произведение заданных элементов равно {product} ')


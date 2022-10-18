# 1. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# 2. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы "привет", "как тебя зовут". 
# Если фраза ему не тзвестна, он выводит соответствующую фразу.

def Fruits():
    file=open("fruits.txt", encoding='utf-8')
    s=file.readlines()
    file.close()
    print(s)

    letter=input("Первая буква для поиска: ")

    for i in s:
        if i[0]==letter.lower() or i[0]==letter:
            print(i, end='')
#Fruits()

file=open("bot.txt", encoding='utf-8')
s=file.readlines()
file.close()

d={}
for i in range(0,len(s),2):
    d[s[i][:-1]]=s[i+1][:-1]

ask=''
print(" После знака ? напиши свой вопрос программе.\n Если программа не знает ответ на твой вопрос- научи ее в следующей строке.\n Когда надоест- напиши стоп. \n К сожалению, пока новые вопросы и ответы можно сохранять только на английском")
while True:
    ask=input('?')
    if ask=="стоп":
        break
   
    elif ask in d:
        print(d[ask])
    else:
        file=open("bot.txt", 'a')
        d[ask]=input("Ответ:")
        file.writelines(ask)
        file.write('\n')
        file.write(d[ask])
        file.write('\n')
        file.close()
    




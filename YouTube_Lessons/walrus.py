# if number := int(input('Введите число: ')) == 100:
#   print('Соточка')
# else:
#   print('Не Соточка')
#
#
# words = input('Введите слова через пробел: ').split()
#
# if (count := len(words)) > 3:
#     print (f"Ого сколько слов вы знаете, аж {count}")
# else:
#     print (f"Словарный запас пополнить надо, {count} это маловато")
#
#
# if (s:=int(input()))<=10000:
#     print(f'Сумма {s} не превышает лимит, проходите')
# else:
#     print(f'Ого! {s}! Куда вам столько? Мы заберем {s-10000}')

#
# if "walrus" in (s:=input()):
#     print("Нашли моржа")
# else:
#     print("Никаких моржей тут нет")



# a=input()
# a=a.rjust(6,'0')
#

# b=int(a[0])+int(a[1])+int(a[2])
# c=int(a[-1])+int(a[-2])+int(a[-3])
# if b==c:
#       print("YES")
# else:
#       print("NO")

a= list(input())
b=list(input())

if (ord(a[0])+int(a[1]))%2  == (ord(b[0])+int(b[1]))%2:

# print(ord(a[0])+int(a[1]))
# print(ord(b[0])+int(b[1]))
    print ("YES")
else:
    print("NO")








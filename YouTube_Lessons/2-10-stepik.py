top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']

top[-1]="Сверхъестественное"

top[2]="Настоящий детектив"
print(top)


s=input().split()
print(f'{s[2]} {s[0][0]}.{s[1][0]}.')

s='\n'.join(input().split())
print(s)
a = input()
b=(a.upper()).split()


print('-'.join(list(b[0])), '-'.join(list(b[1])))

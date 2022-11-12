#Напишите программу, удаляющую из текста все слова, содержащие "абв".

s='Очевидно, абвчевидно что чтоабв такое кодирование кодированиеабв эффективно для дляабв данных, содержащих большое количество серий.'
# print(s.split())

# s2=[i for i in s.split() if "абв" not in i]
# print(' '.join(s2))

# print(*filter(lambda x: not set(x) >=set('абв'), s.split()), sep=' ')

# s=' '.join(filter(lambda x: not('а' in x and 'б' in x and 'в' in x), s.lower().split()))
s=' '.join(filter(lambda x: not'абв' in x, s.lower().split()))
print(s)


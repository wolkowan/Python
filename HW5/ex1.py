#Напишите программу, удаляющую из текста все слова, содержащие "абв".

s='Очевидно, абвчевидно что чтоабв такое кодирование кодированиеабв эффективно для дляабв данных, содержащих большое количество серий.'

s2=[i for i in s.split() if "абв" not in i]

print(' '.join(s2))


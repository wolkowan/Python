#Напишите программу, удаляющую из текста все слова, содержащие "абв".

s='Очевидно, абвчевидно что чтоабв такое кодирование кодированиеабв эффективно для дляабв данных, содержащих большое количество серий.'

s=' '.join(filter(lambda x: not'абв' in x, s.lower().split()))
print(s)
# Вычислить число c заданной точностью d
import random
num= random.uniform(1,5)
degree=random.randint(-10, -1)
d=10**degree
result=round(num, -(degree))
print(f'число {num} точность округления{d} результат {result}')

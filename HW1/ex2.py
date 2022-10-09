
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x=bool(input("x=  "))# ввод в формате 1 или 0
# y=bool(input("y=  "))
# z=bool(input("z=  "))
# print(not (x or y or z))
# print((not x) and(not y)and(not z))


for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print((not (x or y or z)) == ((not x) and (not y) and (not z)))




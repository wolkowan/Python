# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 

num = int(input())
set_prime_multipliers = set()
multiplier = 2
while num > 1:
    if num % multiplier == 0:
        set_prime_multipliers.add(multiplier)
        num = num//multiplier
    else:
        multiplier += 1
print(set_prime_multipliers)

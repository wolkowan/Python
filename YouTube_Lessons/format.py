name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = """Дорогой {0} {1}, 
баланс Вашего лицевого счёта составляет {2} руб.""".format(name, mid_name, balance)

print(text)


name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = """Дорогой {n} {m}, 
баланс Вашего лицевого счёта составляет {b} руб.""".format(m=mid_name, n=name, b=balance)

print(text)


num= int(input())
num1=num-1
num2=num+1
print('''
Для числа {0} предыдущим будет число {1}.
Для числа {0} следующим будет число {2}.'''.format(num,num1,num2))
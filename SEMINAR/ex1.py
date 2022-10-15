import datetime
b1=10
b2=20
a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
a=a%1
new=round(b1+(b2-b1)*a)
print(new)


mas = list(map(chr, range(97, 123)))  
print(mas)
n=15
b1=0
b2=25
a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
a=a%1
s=''
for i in range (10):
    a = a*(datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
    a=(a*1000)%1
    #sleep(1)
    print(a)
    stroka=mas[round(b1+(b2-b1)*a)]
    s+=stroka
print(s)





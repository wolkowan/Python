d=a=int(input())
e=b=int(input())

while b>0:
    c=a%b
    a=b
    b=c
print("NOD= ", a, ", NOK=", (d*e)/a)
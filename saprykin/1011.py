def ex1():

# даны 2 случайных 5-х числа, состоят ли они из одних и тех же цифр
    import random
    from random import randint
    a=random.randint(10000,100000)
    b=random.randint(10000,100000)
    print(a,b)

    print(sorted(list(str(a)))==sorted(list(str(b))))

def ex2():
    def check_number(num):
        return 10000<=num<99999

    a=12351
    b=45236

    if check_number(a) and check_number(b):
       print (set(str(a))==set(str(b)))

    else:
        print('wrong number')

def ex3():
    # выражение дано строкой.Калькулятор.

    a="22+352-5-62+15"
    z=('+','-','/','*')
    def sum(a,b):
        return a+b
    def mult(a,b):
        return a*b
    def subt(a,b):
        return a-b
    def div (a,b):
        return a/b
    a1=''
    a2= []
    operator=[]



    for i in a:
        if i.isdigit():
            a1+=i
        else:
            operator.append(i)
            a2.append(int(a1))
            a1=''
    a2.append(int(a1))

    result=0
    i=0
    while i<len(operator):
        if operator[i]=='+':
            if i==0:
                result = sum(a2[0],a2[2] )
            else:
                result= sum(result, a2[i + 1])


        if operator[i]=='-':
            if i==0:
                result=a2[0]-a2[2]
            else:
                result=result-a2[i+1]
        i+=1

    print(result)
    print(eval(a))

    print(a2)
    print(operator)


def ex4():
    price1=5
    price2=10
    price3=100
    money=1000
    for count1 in range(money//price1):
        for count1 in range(money // price1):
a = [-1,2,-3,4,5,-6]
b=list(map(abs, a))
print(b)
c=[abs(i) for i in a]
print(c)

def F(x):
    return x**2
d= list(map(F,a))
print(d)


s=["hello", "good day", 'Hi']
s1=list(map(str.upper, s))
print(s1)
s2=list(map(lambda x: x+"!!!", s))
print(s2)


s3=list(map(list, s))
s4=list(map(sorted, s3))
print(s4)
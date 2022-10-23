a=[
    ("ivanov", 2002),
    ("Petrov", 1998),
    ("Lukov", 2012),
    ("Pkghl", 1995),
    ("ivfljal", 2022),
    ("Pelhksdjtrov", 1996)
]
print(a[1][0])
b=[i[0] for i in a if i[0].startswith("L")]
print(b)
c=[i[0][0] for i in a if i[1]>2000]
print(c)

d={
    "ivanov": { 'age':2002, "car":"bmw"},
    "Klknfv":  {'age':1998, "car":"bkhjw"},
    "Mjiev": { 'age':2006, "car":"amw"},
    "Anlov":  {'age':1996, "car":"olkjw"},
    "Ubfknov": { 'age':2014, "car":"lomw"},
    "Okjhov":  {'age':2011, "car":"hrjw"},
    "Knlov": { 'age':2008, "car":"ew"},
    "Petrov":  {'age':2002, "car":"ew"},
    }
e=[d[elem]['car'] for elem in d if d[elem]['age']<2000]
print(e)

s='kjbrituglwjbkjbf7467e88989r438h887q3648oif7tr8q'
v= [int(i) for i in s if i.isdigit()]
print(v)

import random
n=4
m=4
x=[[random.randint(1,6) for j in range(m)] for i in range(n)]
print(x)
for i in x:
    print(i)
x2= [x[i][j] for i in range(n) for j in range(m) if i==j]
print("main diagonal", x2)
x3=[x[1][j] for j in range(m)]
print('2 stroka', x3)
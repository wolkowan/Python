a = [10, 20, 30, 40, 50]
for i in enumerate(a):
    print(i)


for index, value in enumerate(a):
    print(index,value)
print()
for index, value in enumerate(a):
    if value%20==0:
        print(index, value)

print()
for index, value in enumerate(a):
    a[index]+=1
print(a)

print()
s='hello'
t= ("apple","banana")
for index, value in enumerate(t):
    print(index,value)


d={"one":"apple", "two":"mango"}
for index, value in enumerate(d,10):
        print(index, value)

for index, value in enumerate(range(10,20), 100):
        print(index, value)


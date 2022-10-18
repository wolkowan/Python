r = lambda x: x ** 2
print(r(7))

perimetr = lambda a, b, c: a + b + c
print(perimetr(1, 2, 3))

h = lambda: "hello"
print(h())

t = lambda x: "positiv" if x > 0 else "negative"
print(t(-5))

# сортировка по почледней цифре в числе:

a = [12, 152, 6000, 128]
a.sort(key=lambda x: x%10)
print(a)


# y=kx+b

def lin(k, b):
    return lambda x: k * x + b


graf1 = lin(2, 5)
print(graf1(3))

# YIELD

def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr*=i
        yield pr
for i in fact(10):
    print(i)


def genf():
    for i in [43,65,48]:
        yield i
for i in genf():
    print(i)

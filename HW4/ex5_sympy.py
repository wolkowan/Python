import re
from sympy import Symbol, collect

s1="161*x**6 + 104*x**5 + 33*x**4 + 75*x**3 + 84*x**2 + 130*x + 79"
s2='77*x**6 + 43*x**5 + 22*x**2 + 49*x + 33'

x=Symbol('x')
s3= collect(s1 + '+' + s2, x)
print(s3)
# #Генераторы и итераторы
#
# s=[1,2,3]
# s1= iter(s)
# print(next(s1))
# print(next(s1))
#
#
# s3=(i**2 for i in range(1,4))
# print("first")
# print(next(s3))
# print(next(s3))
# print(next(s3))
# print("second")
# print(next(s3))
# print(next(s3))
# print(next(s3))


c=(i for i in range(100000))
for i in c:
    print(i)
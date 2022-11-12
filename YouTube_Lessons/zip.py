a=[1,3,5,8,9]
b=[12,13,15,18,19]
c='ghfjk'
#
# res=zip(a,b,c)
# print(list(res))
#
# for t1,t2,t3 in zip(a,b,c):
#     print(t1,t2,t3)


s=zip(a,b,c)
col1, col2, col3 = zip(*s)
print(col1, col2, col3)
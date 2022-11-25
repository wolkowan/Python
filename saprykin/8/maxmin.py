import create_massive_uniq

a= create_massive_uniq.create_matrix_uniq()

res=[]

for i in a:
    for j in i:
        res.append(j)
create_massive_uniq.print_matrix(res)

res.sort()

print(f'{res[-2]}-{res[1]} = {res[-2]-res[1]}')

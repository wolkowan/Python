# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# text = text.encode('utf8')

# with open('file.txt', 'w', encoding = "utf-8") as data:
    # data.write('текст')


def list_from_file(file):
    with open(file, 'r') as data:
        str = data.read()
    pol_list = str.split(' + ')
    return pol_list

def strlist_to_intlist(lst):
    list_of_lst = []

    for i in range(len(lst)):
        if 'x^' in lst[i]:
            list_of_lst.append((lst[i]).split('x^'))
        elif 'x' in lst[i]:
            list_of_lst.append((lst[i]).split('x'))
        else:
            list_of_lst.append([lst[i], '0'])
    
    for j in range(len(list_of_lst)):
        for k in range(len(list_of_lst[i])):
            if list_of_lst[j][k] == '': list_of_lst[j][k] = '1'
            list_of_lst[j][k] = int(list_of_lst[j][k])

    return list_of_lst

def polynomials_sum(lst1, lst2):
    lst_sum = []

    if len(lst1) >= len(lst2):
        for i in range(len(lst1)):
            for j in range(len(lst1[i])):
                for k in range(len(lst2)):
                    for l in range(len(lst2[k])):
                        if lst1[i][j] == lst1[k][l]:
                            lst_sum.append()

    return lst_sum

poly1 = list_from_file('file_HW4_1.txt')
#print(poly1)
#print(f'{strlist_to_intlist(poly1)}\n')
a1=strlist_to_intlist(poly1)
poly2 = list_from_file('file_HW4_2.txt')
a2=strlist_to_intlist(poly2)
print(a1)
print(a2)

           
b=[[i[0]+j[0], i[1]] for i in a1 for j in a2 if i[1]==j[1]]

#print(b)
c= list({i[1]for i in a1 for j in a2}-{j[1]for i in a1 for j in a2})


c1=[[j[0],i] for i in c for j in a1 if i==j[1]]
c2=[[j[0],i] for i in c for j in a2 if i==j[1]]
    
itog= c1+c2+b
print(itog)

h1= [str(i[0]) +'x^'+str (i[1]) for i in itog if i[1]>1]
h2= [str(i[0])+'x' for i in itog if i[1]==1]
h3= [str(i[0]) for i in itog if i[1]==0]
print(h2)
print(h3)
final=''
for i in h1:
    final+=i+' + '
print(f'{final}{str(h2[0])} + {str(h3[0])} = 0')
    
            


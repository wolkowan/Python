
import os
path ="C:\\Muvies"
# print((os.listdir(path)))
# for i in os.listdir(path):
#     print(i, path+'\\'+i)
# for i in os.listdir(path):
#     print(i, path + '\\' + i, os.path.isdir(path + '\\' + i))
file_name= "fruits.txt"
def obhod (path, name, level=1):
    print("Level =", level, ", content: ", os.listdir(path))
    for i in os.listdir(path):

                #print( "файл ", name, "обнаружен по адресу:", ((path+'\\'+i), level+1))
        if os.path.isdir(path+'\\'+i):
            print("Спускаемся: ", path+'\\'+i)
            obhod((path+'\\'+i), level+1)
            print("Возвращаемся в : ", path)



obhod(path, file_name)
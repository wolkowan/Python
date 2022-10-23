s=' Питонабв предостабвавляет  методов определены в математическом модуле'.split()
print(s)
for i in s:
    if "абв" in i:
        print(i)
        i.replace(i, "*****")
print(s)
        

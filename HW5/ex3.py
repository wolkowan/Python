# # 4.4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример
# 	а) AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E

def rle(str):
    result = []
    count = 0
 
    if len(str) == 1:
        result.append((1, str[0]))
        return result
 
    for i in range(len(str)):
        count += 1
        if (i + 1) == len(str) or str[i] != str[i + 1]:
            result.append((count,str[i]))
            count = 0
            
    return result
 

 
str = "AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE"
print(rle(str))
 
    

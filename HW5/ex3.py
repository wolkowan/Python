# # 4.4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример
# 	а) AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E

def RLE_IN(s):
    result = ''
    count = 0
    for i in range(len(s)):
        count += 1
        if (i + 1) == len(s) or s[i] != s[i + 1]:
            result += str(count) + s[i]
            count = 0     
    return result
def RLE_OUT(s):
    result = ''
    for i in range(len(s)):
        
 

 
s = "AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE"
print(RLE_IN(s))
 
    

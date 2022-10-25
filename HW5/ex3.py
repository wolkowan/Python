# # 4.4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример
# 	а) AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E

with open ("RLE_1.txt") as f1:
    s1=f1.read()
with open ("RLE_2.txt") as f2:
    s2=f2.read()

def RLE_IN(s):
    result = ''
    if len(s)<2:
        result=s
    count = 0
    for i in range(len(s)):
        count += 1
        if (i + 1) == len(s) or s[i] != s[i + 1]:
            result += str(count) + s[i]
            count = 0     
    return result


def RLE_OUT(s):
    result =''
    nums=''
    for i in s:
        if i.isdigit():
            nums+=i
        if i.isalpha():
            result+= int(nums)*i
            nums=''
    return result


print(RLE_OUT(s2))
print(RLE_IN(s1))


   
def My_random(count = 1): # фунцкция вывода псевдослучайных чисел заданной разрядности
    import time
    import datetime
    random = ''
    for i in range(1, count + 1):
        random_digit = str((datetime.datetime.now()).microsecond % 10)
        random += random_digit
        time.sleep(0.02)
    return int(random)
a= My_random(count = 5)
print((a))
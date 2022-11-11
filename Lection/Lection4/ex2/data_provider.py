from random import randint
def get_temp(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)

def get_press(sensor):
    return randint(720, 730) if sensor else randint(730-740)


def get_wind(sensor):
    return randint(5,10) if sensor else randint(10, 20)
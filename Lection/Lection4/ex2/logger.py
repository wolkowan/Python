from datetime import datetime



def temp_logger(data):
    time=datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{}; temperature; {}". format(time, data))

def press_logger(data):
    time=datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{}; pressure; {}". format(time, data))

def wind_logger(data):
    time=datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{}; wind speed; {}". format(time, data))
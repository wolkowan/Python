import interface
from datetime import datetime


# logging.basicConfig(
#     level=logging.INFO,
#     filename='phonebook.log',
#     format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
#     datefmt='%d.%m.%Y %H:%M:%S ',


def logger(information):
    time=datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding = "utf-8") as file:
        file.write("{} {} \n". format(time, information))


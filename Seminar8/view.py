


def print_all_to_console():
    with open('employees.csv', 'r') as data:
        for line in data:
            print(line.replace(',', ' '))
            print('\n')

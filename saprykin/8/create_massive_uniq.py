import random
def print_matrix(numbers):
    for i in numbers:
        print(i)


def create_matrix_uniq():

    rows = 4
    columns = 5

    numbers = [0] * rows
    used = []
    for i in range(rows):
        numbers[i] = list(0 for i in range(columns))
    for i in range(rows):
        for j in range(columns):
            current_number = random.randint(0, 30)
            while current_number in used:
                current_number = random.randint(0, 30)
            numbers[i][j] = current_number
            used.append(current_number)
    return numbers



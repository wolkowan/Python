from fractions import Fraction
from math import gcd
import re


def calc(a, b, oper):
    if type(a) == str and type(b) == str:
        if a.find('/') < 0 and b.find('/') < 0:
            a_real = float(a)
            b_real = float(b)
            return operation(a_real, b_real, oper)
        else:
            if a[a.find('/') + 1] == '0' or b[b.find('/') + 1] == '0':
                return 'Деление на ноль'
            else:
                return parce_fraction_answer(operation_fraction(pars_fraction(a), pars_fraction(b), oper))


def operation(n1, n2, oper):
    round_match = max(len(str(n1).split('.')[1]), len(str(n2).split('.')[1]))
    match oper:
        case '+':
            return str(round(n1 + n2, round_match))
        case '-':
            return str(round(n1 - n2, round_match))
        case '*':
            return str(round(n1 * n2, round_match))
        case '/':
            if float(n2) == 0.0:
                return 'Деление на ноль'
            else:
                return str(round(n1 / n2, round_match))


def operation_fraction(n1, n2, oper):
    match oper:
        case '+':
            return f'{Fraction(n1).numerator * Fraction(n2).denominator + Fraction(n2).numerator * Fraction(n1).denominator}/{Fraction(n2).denominator * Fraction(n1).denominator}'
        case '-':
            return f'{Fraction(n1).numerator * Fraction(n2).denominator - Fraction(n2).numerator * Fraction(n1).denominator}/{Fraction(n2).denominator * Fraction(n1).denominator}'
        case '*':
            return f'{Fraction(n1).numerator * Fraction(n2).numerator}/{Fraction(n1).denominator * Fraction(n2).denominator}'
        case '/':
            return f'{Fraction(n1).numerator * Fraction(n2).denominator}/{Fraction(n2).numerator * Fraction(n1).denominator}'


def pars_fraction(number):
    ans_str = re.split(' |/', number)
    sign = ''
    if len(ans_str) > 2:
        if int(ans_str[0]) < 0:
            sign = '-'
            ans_str[0] = f'{abs(int(ans_str[0]))}'
        return f'{sign}{int(ans_str[0]) * int(ans_str[2]) + int(ans_str[1])}/{ans_str[2]}'
    else:
        return number


def parce_fraction_answer(number):
    ans_str = (list(map(int, number.split('/'))))
    sign = ''

    if ans_str[0] < 0:
        sign = '-'
        ans_str[0] = int(ans_str[0]) * -1

    if len(ans_str) < 2:
        return f'{number}'

    elif ans_str[1] == 1:
        return f'{ans_str[0]}'

    elif ans_str[0] == 0:
        return f'{ans_str[0]}'

    elif ans_str[1] == 0:
        return 'Division by zero'

    elif ans_str[0] == ans_str[1]:
        return f'{sign}1'

    elif ans_str[0] > ans_str[1]:
        int_num = int(ans_str[0] / ans_str[1])
        fract_nod = gcd(ans_str[0], ans_str[1])
        ans_str[0] = int(ans_str[0] / fract_nod)
        ans_str[1] = int(ans_str[1] / fract_nod)
        if (ans_str[0] - int_num * ans_str[1]) == 0:
            return f'{sign}{int_num}'
        else:
            return f'{sign}{int_num} {ans_str[0] - int_num * ans_str[1]}/{ans_str[1]}'

    else:
        fract_nod = gcd(ans_str[0], ans_str[1])
        return f'{sign}{ans_str[0] / fract_nod}/{ans_str[1] / fract_nod}'
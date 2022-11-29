def calc(first_arg='', second_arg='', oper=''):
    if second_arg == '0' and oper == '/':
        return "Деление на ноль"

    for i in first_arg:
        if '+' or '-' in i:
            a_complex = complex(first_arg)
            break
        if '+' or '-' not in i:
            a_complex = f'0+{first_arg}'
            complex(a_complex)

    for i in second_arg:
        if '+' or '-' in i:
            b_complex = complex(second_arg)
            break
        if '+' or '-' not in i:
            b_complex = f'0+{second_arg}'
            complex(second_arg)

    match oper:
        case '+':

            result = str(a_complex + b_complex)
            if '1j' in result:
                result.replace('1j', 'j')
            return result
        case '-':
            result = str(a_complex - b_complex)
            if '1j' in result:
                result.replace('1j', 'j')
            return result
        case '*':
            result = str(a_complex * b_complex)
            if '1j' in result:
                result.replace('1j', 'j')
            return result
        case '/':
            result = str(a_complex / b_complex)
            if '1j' in result:
                result.replace('1j', 'j')
                return result
            return result
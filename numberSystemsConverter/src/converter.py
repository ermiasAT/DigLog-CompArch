# this is the nucleus of this project
def decimal_to_binary(decimal):
    comments = ''
    whole = round(decimal // 1)
    frac = decimal - whole
    binary = ''
    while whole != 0 and whole != 1: 
        comments += 'Divide integer part of decimal number by 2:\n'
        comments += f'{whole} / 2 = {whole // 2}\nRemainder = {whole % 2}\n'
        binary = str(whole % 2) + binary
        whole = (whole // 2)
    binary = str(whole % 2) + binary

    if frac != 0: 
        fraction = ''
        while frac != 1 and (len(fraction) + len(binary)) <= 24:
            comments += f'Multiple fraction part of decimal number by 2: \n'
            comments += f'{frac} * 2 = {frac * 2} = '
            frac = frac * 2
            if frac > 1:
                frac = frac - 1
                comments += f'1 + {frac}\n'
                fraction += '1'
            elif frac < 1:
                comments += f'0 + {frac}\n'
                fraction += '0'
        fraction += '1'
        comments += '1\n'
        binary = binary + '.' + fraction

    binary = binary[:24]
    comments += f'The decimal number {decimal} in binary is {binary}'
    return comments, binary

def binary_to_decimal(binary_str):
    split_str = binary_str.split('.')
    whole = split_str[0]
    if len(split_str) > 1:
        frac = split_str[1]
    else:
        frac = []
    decimal = 0
    comments = ''
    comments += f'Multiply each binary digit by 2 to its corresponding power, where the digit on the left of the decimal point(LSB) is 2^0\n'
    comments += f'= '
    for i in range(0, len(whole)): 
        if (i != 0): comments += ' + '
        comments += f'{whole[i]}*2^{(len(whole) - 1 - i)}'
        decimal += float(whole[i])*2**(len(whole) - 1 - i)

    for i in range(0, len(frac)): 
        comments += ' + '
        comments += f'{frac[i]}*2^({-i - 1})'
        decimal += float(frac[i])*2**(-i - 1)

    comments += f'\nThe decimal representation of the binary number {binary_str} is {decimal}'
    return comments, decimal

def hex_to_binary(hex_str):
    comments = 'To convert a number from hex to binary, convert each digit in the hex representation as a 4-bit binary digit. Concatenate the results.\n'
    binary = ''
    conversions = {} 
    for i in range(0, 10):
        conversions[f'{i}'] = str(decimal_to_binary(i)[1]).rjust(4, '0')
    conversions['A'] = str(decimal_to_binary(10)[1]).rjust(4, '0')
    conversions['B'] = str(decimal_to_binary(11)[1]).rjust(4, '0')
    conversions['C'] = str(decimal_to_binary(12)[1]).rjust(4, '0')
    conversions['D'] = str(decimal_to_binary(13)[1]).rjust(4, '0')
    conversions['E'] = str(decimal_to_binary(14)[1]).rjust(4, '0')
    conversions['F'] = str(decimal_to_binary(15)[1]).rjust(4, '0')

    for b in hex_str:
        binary += conversions[b]
        comments += f'{b} in hexadecimal is {conversions[b]} in binary.\n'

    comments += f'The hexadecimal number {hex_str} is {binary} in binary numbers.'
    return comments, binary

def binary_to_hex(binary_str):
    comments = 'To convert a number from binary to hex, convert every FOUR binary digits into a hex digit. Concatenate the results.\n'
    hex = ''
    conversions = {} 
    for i in range(0, 10):
        conversions[str(decimal_to_binary(i)[1]).rjust(4, '0')] = f'{i}'
    conversions[str(decimal_to_binary(10)[1]).rjust(4, '0')] = 'A'
    conversions[str(decimal_to_binary(11)[1]).rjust(4, '0')] = 'B'
    conversions[str(decimal_to_binary(12)[1]).rjust(4, '0')] = 'C'
    conversions[str(decimal_to_binary(13)[1]).rjust(4, '0')] = 'D'
    conversions[str(decimal_to_binary(14)[1]).rjust(4, '0')] = 'E'
    conversions[str(decimal_to_binary(15)[1]).rjust(4, '0')] = 'F'

    if (len(binary_str) % 4 != 0):
        groups = len(binary_str) // 4
        binary_str = binary_str.rjust((groups + 1) * 4, '0')

    i = 0
    groups = []
    while (i < len(binary_str) - 3):
        groups.append(binary_str[i:i+4])
        i += 4
    for group in groups:
        hex += conversions[group]
        comments += f'{group} in hexadecimal is {conversions[group]} in binary.\n'

    comments += f'The hexadecimal number {binary_str} is {hex} in binary numbers.'
    return comments, hex

def hex_to_decimal(hex_str):
    split_str = hex_str.split('.')
    whole = split_str[0]
    if len(split_str) > 1:
        frac = split_str[1]
    else:
        frac = []
    decimal = 0

    conversions = {}
    for i in range(0, 10):
        conversions[f'{i}'] = i
    conversions['A'] = 10
    conversions['B'] = 11
    conversions['C'] = 12
    conversions['D'] = 13
    conversions['E'] = 14
    conversions['F'] = 15

    comments = ''
    comments += f'Multiply each binary digit by 16 to its corresponding power, where the digit on the left of the decimal point(LSB) is 16^0\n'
    comments += f'= '

    for i in range(0, len(whole)): 
        if (i != 0): comments += ' + '
        comments += f'{conversions[whole[i]]}*16^{(len(whole) - 1 - i)}'
        decimal += float(conversions[whole[i]])*16**(len(whole) - 1 - i)

    for i in range(0, len(frac)): 
        comments += ' + '
        comments += f'{conversions[frac[i]]}*16^({-i - 1})'
        decimal += float(conversions[frac[i]])*16**(-i - 1)

    comments += f'\nThe decimal representation of the binary number {hex_str} is {decimal}'
    return comments, decimal

def decimal_to_hex(decimal):
    comments = ''
    whole = round(decimal // 1)
    frac = decimal - whole
    hex = ''

    conversions = {}
    for i in range(0, 10):
        conversions[i] = f'{i}'
    conversions[10] = 'A'
    conversions[11] = 'B'
    conversions[12] = 'C'
    conversions[13] = 'D'
    conversions[14] = 'E'
    conversions[15] = 'F'

    while whole != 0 and whole != 1: 
        comments += 'Divide integer part of decimal number by 16:\n'
        comments += f'{whole} / 16 = {whole // 16}\nRemainder = {conversions[whole % 16]}\n'
        hex = conversions[whole % 16] + hex
        whole = (whole // 16)
    hex = conversions[whole % 16] + hex

    if frac != 0: 
        fraction = ''
        while frac < 16 and (len(fraction) + len(hex)) <= 24 and frac != 0:
            comments += f'Multiple fraction part of decimal number by 16: \n'
            comments += f'{frac} * 16 = {frac * 16} = '
            frac = frac * 16
            if frac > 1:
                comments += f'{frac // 1} + {frac - frac // 1}\n'
                fraction += conversions[frac // 1]
                frac = frac - frac // 1
            elif frac < 1:
                comments += f'0 + {frac}\n'
                fraction += '0'
        comments += '1\n'
        hex = hex + '.' + fraction

    hex = hex[:24]
    comments += f'The decimal number {decimal} in hexadecimal is {hex}'
    return comments, hex

def is_valid_decimal(s):
    try:
        float(s)
        return True
    except:
        return False

def is_valid_binary(s):
    return all(c in '01' for c in s)

def is_valid_hex(s):
    try:
        int(s, 16)
        return True
    except:
        return False

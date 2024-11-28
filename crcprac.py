def xor(a,b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp

def encode_data(data, key):
    len_key = len(key)
    append_data = data + '0' * (len_key - 1)
    remainder = mod2div(append_data, key)
    codeword = data + remainder
    return codeword


print(encode_data('100100' , '1010'))


def verify_data(data, key):
    remainder = mod2div(data, key)
    if '1' in remainder:
        return 'Error'
    else:
        return 'Correct'
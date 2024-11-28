def xor(a, b):
    # Perform XOR operation on two binary strings
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    # Perform Modulo-2 division and return the remainder
    pick = len(divisor)
    tmp = dividend[:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    # Perform division for the last bit
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp

def encode_data(data, key):
    # Append zeros to the data to match divisor length
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

# Example Usage
data = '100100'  # Binary data to encode
key = '1010'        # CRC polynomial divisor

print("Original Data: ", data)
print("Divisor (Polynomial): ", key)

# Encode data with CRC
encoded_data = encode_data(data, key)
print("Encoded Data (with CRC): ", encoded_data)

# Verifying the data
def verify_data(data, key):
    remainder = mod2div(data, key)
    if '1' in remainder:
        return "Data is corrupted"
    else:
        return "Data is valid"

# Checking the encoded data for correctness
print("Verification: ", verify_data(encoded_data, key))

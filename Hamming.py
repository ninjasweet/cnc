def hamming_encode(data):
    n, r = len(data), 0
    while (2 ** r) < (n + r + 1): r += 1
    code = [0] * (n + r)
    j = 0
    for i in range(1, len(code) + 1):
        if i & (i - 1): code[i - 1] = data[j]; j += 1
    for i in range(r):
        pos = 2 ** i
        code[pos - 1] = sum(code[j] for j in range(len(code)) if j & pos == pos - 1) % 2
    return code

def hamming_decode(code):
    r = len(bin(len(code))) - 2
    error_pos = sum((sum(code[j] for j in range(len(code)) if j & (1 << i)) % 2) * (1 << i) for i in range(r))
    if error_pos: code[error_pos - 1] ^= 1
    return [code[i] for i in range(len(code)) if i & (i + 1)]

# Example usage
data = [1, 0, 0, 0]
encoded = hamming_encode(data)
print("Encoded:", encoded)
encoded[3] ^= 1  # Introduce an error
print("Received with error:", encoded)
decoded = hamming_decode(encoded)
print("Decoded (corrected):", decoded)

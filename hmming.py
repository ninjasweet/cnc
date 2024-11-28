def hamming_encode_4bit(data_bits):
    hamming_code = ['0'] * 7

    # Assign data bits to positions 3, 5, 6, 7 (1-based index)
    hamming_code[2] = data_bits[0]  # Position 3
    hamming_code[4] = data_bits[1]  # Position 5
    hamming_code[5] = data_bits[2]  # Position 6
    hamming_code[6] = data_bits[3]  # Position 7

    # Calculate parity bits
    hamming_code[0] = str(int(hamming_code[2]) ^ int(hamming_code[4]) ^ int(hamming_code[6]))  # P1 (Position 1)
    hamming_code[1] = str(int(hamming_code[2]) ^ int(hamming_code[5]) ^ int(hamming_code[6]))  # P2 (Position 2)
    hamming_code[3] = str(int(hamming_code[4]) ^ int(hamming_code[5]) ^ int(hamming_code[6]))  # P4 (Position 4)

    return ''.join(hamming_code)


def hamming_decode_7bit(hamming_code):
    p1 = int(hamming_code[0]) ^ int(hamming_code[2]) ^ int(hamming_code[4]) ^ int(hamming_code[6])  # P1 check
    p2 = int(hamming_code[1]) ^ int(hamming_code[2]) ^ int(hamming_code[5]) ^ int(hamming_code[6])  # P2 check
    p4 = int(hamming_code[3]) ^ int(hamming_code[4]) ^ int(hamming_code[5]) ^ int(hamming_code[6])  # P4 check

    error_position = p1 * 1 + p2 * 2 + p4 * 4

    # Correct error if needed
    if error_position:
        print(f"Error detected at position {error_position}. Correcting...")
        hamming_code = list(hamming_code)
        hamming_code[error_position - 1] = '1' if hamming_code[error_position - 1] == '0' else '0'
        hamming_code = ''.join(hamming_code)
    else:
        print("No errors detected.")

    # Extract original data bits from positions 3, 5, 6, 7
    original_data = hamming_code[2] + hamming_code[4] + hamming_code[5] + hamming_code[6]

    return original_data


# Example Usage
data = "1011"  # Input 4-bit data
print(f"Original Data: {data}")

encoded = hamming_encode_4bit(data)
print(f"Encoded Hamming Code: {encoded}")

# Introduce an error for testing
encoded_with_error = encoded[:3] + ('1' if encoded[3] == '0' else '0') + encoded[4:]
print(f"Encoded with Error: {encoded_with_error}")

decoded = hamming_decode_7bit(encoded_with_error)
print(f"Decoded Data: {decoded}")

import math
import random
def RSA(num1, num2):
    n = num1 * num2
    phi = (num1 - 1) * (num2 - 1)
    e = random.randint(2, phi-1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi-1)
    d = pow(e, -1, phi)
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key
def Encrypt(public_key, msg):
    e, n = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in msg]
    return encrypted_msg
def Decrypt(private_key, encrypted_msg):
    d, n = private_key
    decrypted_msg = "".join([chr(pow(char, d, n))for char in encrypted_msg])
    return decrypted_msg
def main():
    num1 = 13
    num2 = 17
    public_key, private_key = RSA(num1, num2)
    msg = "Jenish"
    encrypted_msg = Encrypt(public_key, msg)
    decrypted_msg = Decrypt(private_key, encrypted_msg)
    print(public_key, private_key)
    print(msg)
    print(encrypted_msg)
    print(decrypted_msg)
if __name__ == '__main__':
    main()
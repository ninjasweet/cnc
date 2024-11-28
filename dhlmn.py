import math

def dhlmn(x, y, z):
    return pow(x, y, z)

g = 3
p = 17

pvt_a = 15
pvt_b = 13

pub_a = dhlmn(g, pvt_a, p)
pub_b = dhlmn(g, pvt_b, p)

shared_a = dhlmn(pub_b, pvt_a, p)
shared_b = dhlmn(pub_a, pvt_b, p)

print(g, p)
print(pub_a, pub_b)
print(shared_a, shared_b)

if shared_a == shared_b:
    shared_secret = shared_a

def encrypt_message(message, shared_secret):
    return ''.join([chr(ord(c) ^ shared_secret) for c in message])

def decrypt_message(encrypted_message, shared_secret):
    return ''.join([chr(ord(c) ^ shared_secret) for c in encrypted_message])


print(encrypt_message("Hello", shared_secret))

print(decrypt_message("Boffe", shared_secret))
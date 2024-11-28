import math
import random
def Diffie_Hellman(num1, num2, num3):
    return pow(num1, num2, num3)
param_1 = 3
param_2 = 17

private_a = 15
private_b = 13

#private_a = 15 #random.randint(2, param_2 - 1)
#private_b = 13 #random.randint(2, param_2 - 1)
public_a = Diffie_Hellman(param_1, private_a, param_2)
public_b = Diffie_Hellman(param_1, private_b, param_2)
shared_a = Diffie_Hellman(public_b, private_a, param_2)
shared_b = Diffie_Hellman(public_a, private_b, param_2)
print(private_a, private_b)
print(public_a, public_b)
print(shared_a, shared_b)
assert shared_a == shared_b
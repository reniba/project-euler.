import math
def isprime(num):
    for a in range(2,math.floor(num**0.5)+1):
        if num % a == 0:
            return False
#        else:
    return True

soma = 0
for n in range(3,2000000,2):
    if isprime(n):
        soma += n
print(soma + 2)

import math

def sum_proper_divisions(number):
    soma = 0
    if number == 1:
        return 1
    for a in range(1,number//2+1):
        if number % a == 0:
            soma += a
    return soma

def is_abundant(number):
    if sum_proper_divisions(number) > number:
        return True
    else:
        return False

a = []
for x in range(1,28124):
    if is_abundant(x):
        a.append(x)

set1 = set()
for m in range(0,len(a)):
    for n in range(0,len(a)):
        if a[m] + a[n] <= 28123:
            set1.add(a[m]+a[n])

print((28123*28124//2) - sum(set1))
            
    


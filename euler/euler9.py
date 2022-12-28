#import fatorar
#primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
#from itertools import combinations
#for item in list(combinations(primos,2)):
#    a = item[1]**2 - item[0]**2
#    b = item[1]*item[0]*2
#    c = item[1]**2 + item[0]**2
#    if a + b + c in fatorar.fatorar(1000):
#        print(a,b,c)

for a in range(0,501):
    for b in range(0,501):
        for c in range(0,501):
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    print(a,b,c)

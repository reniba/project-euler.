#soma = 0
#for n in range(1,101):
#    soma += n**2
#print(soma)
#
#quadrado = 0
#for n in range(1,101):
#    quadrado += n
#print(quadrado**2)
#print(quadrado**2 - soma)
from itertools import combinations
soma = 0
for n in list(combinations(range(1,101),2)):
    soma += 2*n[0]*n[1]
print(soma)

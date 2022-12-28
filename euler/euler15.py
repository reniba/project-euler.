numerador = 1
for n in range(40,20,-1):
    numerador *= n
denominador = 1
for p in range(20,0,-1):
    denominador *= p
print(numerador/denominador)

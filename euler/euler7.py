import fatorar
contador = 1
n = 1
#for n in range(1,10002,2):
while contador != 1000:
    if len(fatorar.fatorar(n))==2:
        contador += 1
        print(n,contador)
    n += 2

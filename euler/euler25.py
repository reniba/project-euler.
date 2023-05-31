from time import time


t0= time()
lista = [1,1]
contador = 2
for n in range(10000):
    lista.append(lista[-1]+lista[-2])
    lista.pop(0)
    contador += 1
    if len(str(lista[1])) == 1000:
        print(contador)
        break
t1 = time() - t0
print(t1)
# CPU seconds elapsed (floating point)
#contador = len_number = 0
#while len_number != 1000:
#    len_number = len(str(fibonacci(contador+1)))
#    contador += 1
#    print(contador,fibonacci(contador))

def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fibo(n-1) + fibo(n-2)

soma = 0
contador = 1
while fibo(contador) < 4000000:
    if fibo(contador) % 2 == 0:
        soma += fibo(contador)
    contador += 1
    


print(contador,fibo(contador),soma)
    
    

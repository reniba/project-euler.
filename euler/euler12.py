
import fatorador as ft
def soma(n):
    if n% 2 == 0:
        return [int(n/2),n+1]
    else:
        return [int((n+1)/2),n]

def numdiv(lista):
    tot = 1
    for num in lista:
        tot *= (num+1)
    return tot



for n in range(2,1000000):
    x,y = soma(n)
    cont = {}
    for number in ft.fatorador(x)+ft.fatorador(y):
        if number not in cont:
            cont[number] = 0
        cont[number] += 1
    if numdiv(cont.values()) >= 500:
        print(n*(n+1)*0.5)
        break

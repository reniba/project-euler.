#euler14
import operator
def arvore(n):
    a = n
    x = 0
    while n != 1:
        if n % 2 == 0:
            x += 1
            n = n//2
        else:
            x += 1
            n = 3*n + 1
    x += 1
    return (x,a)

print(max(map(arvore,range(1,1000001))))

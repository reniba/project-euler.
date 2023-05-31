from math import sqrt
from itertools import compress

abundant_nos = []
for i in range(12,28123):
    factor = 0
    for j in range(2,int(sqrt(i))+1):
        if i%j == 0:
            factor+= j + i//j
            if j == sqrt(i):
                factor -= j
    if factor>i:
        abundant_nos.append(i)
num_list = [True]*28123
k = 0
for i in abundant_nos:
    for j in abundant_nos[k:]:
        if(i+j>28123): break
        num_list[i+j-1] = False
    k+=1
answer = sum(compress(range(1,28124),num_list))

print(answer)

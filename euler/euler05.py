#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 1  2  3  4 ....... 16 17 18 ......n
import fatorar

num = 1
for n in range(1,21):
    if num % n == 0:
        continue
    else:
        if len(fatorar.fatorar(n)) == 2: 
            num *= n
        else:
            num *= fatorar.fatorar(n)[1]
    print(n,num)
print(num)

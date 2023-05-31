def ProperDivisors(number):
    divisors = []
    for a in range(1,number//2+1):
        if number % a == 0:
            divisors.append(a)
    return divisors


answer = 0
for n in range(1,10001):
    a = sum(ProperDivisors(n))
    if sum(ProperDivisors(a)) == n:
        if n > a:
            answer += (n+a)
print(answer)

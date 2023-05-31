def MAIORdivisor(num):
    divisores = []
    divisor = 2
    while True:
        if num % divisor == 0:
            num /= divisor
            divisores.append(divisor)
        divisor += 1
        if num / divisor < 1:
            break
    return(max(divisores))


print(MAIORdivisor(600851475143))

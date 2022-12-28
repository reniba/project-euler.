mul3 = set()
mul5 = set()
for n in range(1000):
    if n % 3 == 0:
        mul3.add(n)
    if n % 5 == 0:
        mul5.add(n)
print(sum(mul3.union(mul5)))

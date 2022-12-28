maior = 0
for n in range(999,800,-1):
    for m in range(999,800,-1):
        t = str(m*n)
        if len(str(t))== 6:
            if t[0:3] == t[-1:-4:-1]:
                if int(t) > maior:
                    maior = int(t)
        else:
            pass
print(maior)

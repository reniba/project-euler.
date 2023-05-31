import itertools as it
x = enumerate(list(it.permutations(['0','1','2','3','4','5','6','7','8','9'])),start=1)
for a,b in x:
    if a == 1000000:
        print(''.join(b))
        break

#import itertools as it
#count = 0
#for perms in it.permutations(list(range(10))):
#    count += 1
#    if count == 1000000:
#        print(perms)
#        break   

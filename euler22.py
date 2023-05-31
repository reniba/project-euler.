
def sumalpha(string):
    """return the sum of the alphabetical positions of each charactere"""
    total = 0
    for letter in string:
        total += alphadic[letter]
    return total


arquivo = open(r'maindirectory\euler022_names.txt', 'r')


alphadic = {}
counter = 1
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    alphadic[letter] = counter
    counter += 1


answer = 0
for line in arquivo:
    aux = sorted(line.replace('"', '').split(','))
    aux2 = list(enumerate(aux,start=1))
    for item in aux2:
        answer += (item[0]*sumalpha(item[1]))

        
arquivo.close()

print(answer)

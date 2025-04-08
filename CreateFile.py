import random
alf = 'ABCDEFGH'

with open('7-1.txt','w') as fout:
    for i in range(10):
        fout.write(random.choice(alf))
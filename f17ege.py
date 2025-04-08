with open('EGE_17.txt') as fin:
    a = [int(i) for i in fin]

n = len(a)
b = []
for i in range(n - 1):
    x,y = a[i], a[i+1]
    if x % 9 == 0 and y % 9 == 0:
        b.append(x + y)
print(len(b),min(b))

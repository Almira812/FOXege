with open('22-1.csv') as fin:
    data = []
    for s in fin: #делаем список
        line = s.split(';')
        data.append([int(line[1]), [int(i) - 1 for i in line[2:]]])

def f(id):
    start = 0 #Время начинается с нуля
    proc = data[id] #Это процессор, id его номер
    for i in proc[1]:
        if i != -1:
            start = max(start,f(i))
    return start + proc[0]

ans = 0
for i in range(len(data)):
    print(i,f(i))
    ans = max(ans,f(i))
print(ans)
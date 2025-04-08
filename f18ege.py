# with open('p1.csv') as fin: #переделали табл.файл в .csv формат
#     a = [float(i.replace(',','.')) for i in fin]
#
# print(a)
# ans = cur = a[0]
# for i in range(1, len(a)):
#     if a[i] < a[i - 1]:
#         cur += a[i]
#         ans = max(ans,cur)
#     else:
#         cur = a[i]
# print(ans)

#сбор монет
# with open('python1.csv') as fin:
#     a = [[int(i) for i in line.split(';')] for line in fin]
#
# n = len(a) #кол-во строк
# m = len(a[0]) #кол-во столбцов
#
# dp = [[0 for i in range(m)] for j in range(n)] #строим таблицу
# dp[0][0] = a[0][0]
#
# for j in range(1, m):
#     dp[0][j] = dp[0][j-1] + a[0][j] #заполнение первой строки
#
# for i in range(1, n):
#     dp[i][0] = dp[i-1][0] + a[i][0] #заполнение первого столбца
#
# for i in range(1,n):
#     for j in range(1,m):
#         dp [i][j] = max(dp[i - 1][j], dp[i][j - 1]) + a[i][j] #заполнение всего остального
#
# for line in dp: #вывод таблицы
#     print(*line)
#
# print(dp[-1][-1])
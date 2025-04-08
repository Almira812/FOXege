# fin = open('text.txt', 'r', encoding='utf8') #utf8 настройка на ru
# #s = fin.read() #все строки
# s = fin.readline() #одна строка
# print(s)
# fin.close()


# with open('text.txt') as fin:
#      a = fin.read()
#     #a = fin.read().splitlines() # превращает в список, не переходя на новую строку
# print(a)

# import sys
# sys.stdin = open('text.txt','r') #всё что будет введено в текстовый файл, то и выведится?
# n = input()
# print(n)



#?кол-во строк, в которых 'K' встречается чаще, чем 'U'
# with open('24-s1.txt') as fin:
#     ans = 0
#     for s in fin: #перебираем каждую строку отдельно
#         if s.count('K') > s.count('U'):
#             ans += 1
# print(ans)

#?длина самой длиной подцепочки из 'Z'
#1 Очень плохой
# Просто открыть файл и ctrl+f
#2 Неочень хороший
# with open('1.txt') as fin:
#     s = fin.read() #читаем строку
#
# ans = 1
# while 'Z' * ans in s:
#     ans += 1
# print(ans-1) #7
#3 Универсальный вариант
# with open('1.txt') as fin:
#      s = fin.read()
# ans = 0
# cur = 0 # длина цепочки из Z
# for c in s: #смотрим на каждый символ
#     if c == 'Z':
#         cur += 1
#         if cur > ans:
#             ans = cur
#     else: #цепочка из Z оборвалась
#         # if cur > ans: #Работает неправильно,
#         #     ans = cur # если нужная цепочка находится в конце
#         cur = 0
# print(ans)

#?максимально кол-во идущих подряд символов,
#?среди которых каждые два соседних различны
# with open('1.txt') as fin:
#     s = fin.read()
#
# ans = 0
# cur = 1 #длина текущей цепочки
# for i in range(1, len(s)):
#     if s[i] != s[i - 1]:
#         cur += 1
#         ans = max(ans,cur)
#     else:
#         cur = 0
# print(ans)
#Для проверки можно создать доп файл, и сделать строку поменьше

#?строку, содержащую самую длинную цепочку стоящих
# подряд одинаковых букв. Если таких строк несколько,
# надо взять ту, которая в файле встретилась раньше.
#? какая буква встречается в этой строке реже всего
# (но присутствует!). Если таких букв несколько,
# надо взять ту, которая стоит последней в алфавите.
#Запишите в ответе эту букву, а затем,
# без пробела – сколько раз она встречается во всем файле.
# with open('24-164.txt') as fin:
#     s = fin.read() #открыли целеком
# lst = s.splitlines() #разделили на строки
#
# i_ans1 = 0 #номер строки для подзадачи 1
# ans1 = 0 #длина самой длиной цепочки
# for j in range(len(lst)): #самая длиная цепочку идущих подряд символов
#     st = lst[j]
#     ans = 1
#     cur = 1
#     for i in range(1, len(st)):
#         if st[i] == st[i-1]:
#             cur += 1
#             ans = max(ans,cur)
#         else:
#             cur = 1
#     if ans > ans1:
#         ans1 = ans
#         i_ans1 = j
#
# print(i_ans1) #номер строки, содержащая самую длинную цепочку стоящих подряд одинаковых букв
#
# st1 = lst[i_ans1] #та самая строка
# alf = 'QWERTYUIOPASDFGHJKLZXCVBNM'
# cnt_ans2 = len(st1)
# ans2  = ''#редкий символ
# for c in alf:
#     cnt = st1.count(c)
#     if cnt > 0 and cnt < cnt_ans2:
#         cnt_ans2 = cnt
#         ans2 = c
# print(ans2, s.count(ans2),sep='') #ответ


#?Найти длину самой длинной цепочки, в которой
# ни одна гласная буква не стоит рядом с согласной.
# Алфавит ABCDEFGH
# glas = 'AE'
# with open('7-1.txt') as fin:
#     s = fin.read()
#
# cur = 1
# ans = 1
# for i in range(1, len(s)):
#     x,y = s[i - 1], s[i]
# #    if x in glas and y  in glas
#     if (x in glas) == (y in glas):
#         cur += 1
#         ans = max(ans, cur)
#     else:
#         cur = 1
# print(ans)

#?Найдите длину самой длинной подцепочки,
# в которой есть ровно три буквы F, не обязательно стоящие рядом
# F = open('Zadanie-260283.txt', 'r')
# st = F.readline()
# z = []
# z.append(-1)
# for i in range(len(st)):
#     if st[i] == 'F':
#         z.append(i) #записываем индексы всех F
#
# z.append(len(st))
#
# mx = 0
# for i in range(2, len(z) - 2):
#     if z[i+2] - z[i-2] > mx: # смотрим расстояние между самыми
#                                   #дальними F
#         mx = z[i+2] - z[i-2]
#         z1 = z[i+2]
#         z2 = z[i-2]
#         print(mx,z1,z2)
# if len(z) > 4: # F должно быть хотя бы две штуки
#     print(len(z))
#     print(mx - 1)
# else:
#     print(0)
# F.close()



# from functools import cache
# @cache
#
# def f(s, n):
#    if s < 10:
#       return ['-', 0]
#    res = []
#    res.append(f(s - 1, n + 1))
#    if s % 2 == 0:
#       res.append(f(s // 2, n + 1))
#    if s % 3 == 0:
#       res.append(f(s - (s // 3), n + 1))
#    win = []
#    lose = []
#    for m in res:
#       if m[0] == '-':
#          win.append(m[1])
#       else:
#          lose.append(m[1])
#    if n == 1 and lose:
#       return ['-', min(lose)]
#    if win:
#       return ['+', min(win) + 1]
#    return ['-', max(lose)]
# for s in range(10, 100):
#    print(s, f(s, 1))


# 8
# from itertools import *
# k = 0
# for i in product('0123456789aaaaa', repeat=5):
#     s = ''.join(i)
#     if s[0] != 0 and s.count('8') == 1 and s.count('a') >= 2:
#         k += 1
# print(k)



# n = int(input())
# k = int(input())
# p1 = int(input())
# p1 *= (n+1)//2
# n = n-p1
# p = [0] *(n+1)
# ps = 0
# s = 0
# for i in range(1,k):
#     ps += int(input())
#     d = 2**i
#     for j in range(2**(i-1),n,d):
#         p[j] = ps
#         s += ps
# print(s+p1)

# n = int(input())
# k = int(input())
# d = []
# for i in range(k):
#     d.append(int(input()))
# d.sort()


# n = int(input())
# m = int(input())
# a = set()
# for i in range(min(n,m)):
#     a.add((1 + i, 1 + i))
# for i in range(min(n,m)):
#     a.add((1 + i, m - i))
# for i in range(min(n,m)):
#     a.add((n - i, 1 + i))
# for i in range(min(n,m)):
#     a.add((n - i, m - i))
#
# print(len(a)-4)

# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return f(n-1) -2*g(n-1)
# def g(n):
#     if n == 1:
#         return 1
#     else:
#         return f(n-1) + g(n-1) + n
# print(sum(int(i) for i in str(g(36))))
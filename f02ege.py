# from itertools import *
# n = 0
# for x,y,z,w in product([0,1], repeat = 4):
#     f = bool((not x or y or z) and (x or not z or not w))
#     if not f:
#         print(x,w,z,y,f)

#Логическая функция F задаётся выражением ¬x ⋁ y ⋁ (¬z ⋀ w). На рисунке приведён
#фрагмент таблицы истинности функции F, содержащий все наборы аргументов, при
#которых функция F ложна. Определите, какому столбцу таблицы истинности функции F
#соответствует каждая из переменных x, y, z, w.
# from itertools import product
# def f(x,y,w,z):
#     return ((not x) or y or ((not z) and w))
#
# print('w x y z')
# for w, x, y, z in product([0,1], repeat=4):
#     if not f(w,x,y,z):
#         print(w,x,y,z)

# print('x w y z')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 if (y or(w and (not z)) or (x and (not w))) == 0:
#                     print(x,w,y,z)

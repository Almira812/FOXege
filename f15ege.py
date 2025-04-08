# for A in range(1,10000):
#     if all((((x%84==0 and x%90==0) or x%A!=0))
#         for x in range(10000)):
#             print (A)
#             break

#?Наименьшее А (ДЕЛ(x, 7) → ¬ДЕЛ(x, 5)) or (x + A ≥ 80)
#ДЕЛ(n, m) - n делится без остатка на m
#тождественно истинна (т.е. принимает значение 1) для всех натуральных x
# def f(x,a):
#     return (int(x % 7 == 0) <= int(x % 5 != 0)) or (x + a >= 80)
#
# for a in range(1, 100):
#     if all(f(x,a) for x in range(1, 1000)):
#         print(a)
#         break

#?Наименьшее А
# (x ≥ 7) ⋁ (2x < y) ⋁ (x ⋅ y < A)
#истинно для любых целых положительных значений x и y.
# def f(x, y):
#     return (x >= 7) or (2*x < y) or (x * y < a)
#
# for a in range(1, 100):
#     if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
#         print(a)
#         break

#?Наибольшее А
# ((x ≤ 3) → (x^2 ≤ A) ) ⋀ ((y^2 ≤ A) → (y ≤ 3))
# def f(x, y, a):
#     return (x > 3 or x ** 2 <= a) and (y ** 2 > a or y <= 3)
#
# for a in range(100): #1
#     flag = True
#     for x in range(1,1000):
#         for y in range(1, 1000):
#             if not f(x, y, a):
#                 flag = False
#     if flag:
#         print(a)

# for a in range(100):  #2
#     ans = True
#     for x in range(1,1000):
#         for y in range(1, 1000):
#             ans &= f(x,y, a)
#     if ans:
#         print(a)


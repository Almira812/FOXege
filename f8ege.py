#?кол-во слов из трех букв из слова 'школа',
#где 'к' встречается ровно один раз
# import itertools
#
# alf = 'школа'
# ans = 0
#
# for i in itertools.product(alf, repeat=3):
#     if i.count('к') == 1:
#         print(i)
#         ans += 1
# print(ans)

#перестановка = permutations
# import itertools
#
# alf = 'капкан'
# ans = set()
# for i in itertools.permutations(alf, len(alf)):
#     s = ''.join(i)
#     if not 'аа' in s and not 'кк' in s:
#         ans.add(s)
#
# print(len(ans))

#Каждую букву нужно использовать ровно один раз
# import itertools
#
# alf = 'вуаль'
# ans = 0
# for i in itertools.permutations(alf):
#     s = ''.join(i)
#     if s[0] != 'ь' and 'ьа' not in s and 'ьу' not in s:
#         ans += 1
#         print(s)
# print(ans)

#5-буквенные слова из 'слон',
# так как слово состоит только из 4 букв
# используем product(можно задать длину больше, чем кол-ва букв)
# import itertools
#
# alf = 'слон'
# ans = 0
# for i in itertools.product(alf,repeat = 5):
#     if i.count('с') == 1:
#         ans += 1
#         print(''.join(i))
# print(ans)

#?Слово на 67-м месте
# import itertools
#
# alf = 'клрт'
# #print(list(itertools.product(alf,repeat = 4))[66]) #много памяти использует
#
# for i, val in enumerate(itertools.product(alf,repeat = 4)):
#     if i == 66:
#         print(val)
#         break

#?На каком месте 'укара'
# import itertools
#
# alf = 'акру'
# for i, val in enumerate(itertools.product(alf, repeat=5)):
#     if ''.join(val) == 'укара':
#         print(i+1)
#         break

#?Сколько слов между словами печалька и печенька, не включая их
# from itertools import product
#
# alf = 'аеклнпчь'
# for i, val in enumerate(product(alf, repeat=8)):
#     s = ''.join(val)
#     if s == 'печалька':
#         start = i
#     elif s == 'печенька':
#         end = i
#
# print(end - start - 1)

#?Определите количество пятизначных чисел, записанных в восьмеричной системе счисления,
# в записи которых только одна цифра 6,
# при этом никакая нечётная цифра не стоит рядом с цифрой 6
# from itertools import product
# k = 0
# n = ['16','36','56','76','61','63','65','67'] #сочетания, которых не должно быть
# alf = '01234567'
# for p in product(alf, repeat = 5):
#     s = ''.join(p)
#     if s[0] != '0' and s.count('6') == 1 and sum([int(x in s) for x in n]) == 0:
#                                           #если нет сочитания, которого не должно быть
#         k += 1
# print(k)

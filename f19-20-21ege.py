#Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит
#ОДНА куча камней. Первый ход делает Петя. За один ход игрок может добавить
#в кучу один камень или увеличить количество камней в куче в два раза.Игра завершается в тот момент,
#когда количество камней в куче становится не менее 29. Победителем считается игрок, сделавший
#последний ход, т.е. первым получивший кучу, в которой будет 29 или больше камней.
#В начальный момент в куче было S камней, 1 ≤ S ≤ 28.
#19? Значение S, при котором Петя не может выиграть за один ход, но при любом ходе
# Пети Ваня может выиграть своим первым ходом.
#20? Найдите два таких значения S, при которых у Пети есть выигрышная стратегия, причём
# одновременно выполняются два условия:
# − Петя не может выиграть за один ход;
# − Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
#21? Найдите значение S, при котором одновременно выполняются два условия:
# – у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при
# любой игре Пети;
# – у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
# def f(s): # То что расписывали в табличке
#     if s >= 149:
#         return ['-',0]
#     moves = []              #получившиеся шаги противника
#     moves.append(f(s + 1))
#     moves.append(f(s * 2))
#     win = []
#     lose = []
#     for move in moves:
#         if move[0] == '-': #если нашли проиграшную позицию для противника
#             win.append(move[1])
#         else:
#             lose.append(move[1])
#     if win:                   #Если в списке win что-то есть
#         return['+', min(win) + 1] #то позиция выигрышная
#     return ['-', max(lose)]       #иначе нет
#
# for s in range(1, 149):
#     print(s, f(s))


#ДВЕ КУЧИ камней - 5, 1 <= s <= 57
#Первый ход - Петя. Ходы - +1 и *2
#Победа - Сумма двух кучек >= 32
#?19 Известно, что Ваня выиграл своим первым ходом после неудачного хода Пети. Укажите
#минимальное значение S, когда такая ситуация возможна.
#1-П  1-В  2-П  2-В  WIN!!!
#?20 Найдите два таких значения S, при которых
# у Пети есть выигрышная стратегия, причём
# одновременно выполняются два условия:
# − Петя не может выиграть за один ход;
# − Петя может выиграть своим вторым ходом независимо
# от того, как будет ходить Ваня.
# Найденные значения запишите в ответе в порядке возрастания.
#?21 Найдите минимальное значение S, при котором одновременно выполняются два условия:
# – у Вани есть выигрышная стратегия,
# позволяющая ему выиграть первым или вторым ходом
# при любой игре Пети;
# – у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
#
# import functools #использование киширования, чтобы быстрее работал
#
# @functools.cache #для мулизации функции
#
# # def f(s1, s2, n): #n - номер хода, для ?19
# def f(s1, s2):
#     if s1 + s2 >= 63:
#         return['-', 0]
#     res = []
#     # res.append(f(s1 + 1, s2, n + 1)) #для ?19
#     # res.append(f(s1 * 2, s2, n + 1))
#     # res.append(f(s1, s2 + 1, n + 1))
#     # res.append(f(s1, s2 * 2, n + 1))
#     res.append(f(s1 + 1, s2))
#     res.append(f(s1 * 2, s2))
#     res.append(f(s1, s2 + 1))
#     res.append(f(s1, s2 * 2))
#     win = []
#     lose = []
#     for move in res:
#         if move[0] == '-':
#             win.append(move[1])
#         else:
#             lose.append(move[1])
#     # if n == 1 and lose: #Петя делает очень плохой ход. Если есть хотя бы один прооигрывающий ход
#     #     return ['-', min(lose)] #и стремиться проиграть как можно быстрее, для ?19
#     if win:
#         return ['+', min(win) + 1]
#     return ['-', max(lose)]
#
# for s in range(1,58):
#     # print(s, f(5, s, 1)) #для ?19
#     print(s, f(5, s))


# import functools #использование киширования, чтобы быстрее работал
#
# @functools.cache #для мулизации функции
#
# # def f(s1, s2, n): #n - номер хода, для ?19
# def f(s1, s2):
#     if s1 + s2 >= 65:
#         return['-', 0]
#     res = []
#     # res.append(f(s1 + 1, s2, n + 1)) #для ?19
#     # res.append(f(s1 * 2, s2, n + 1))
#     # res.append(f(s1, s2 + 1, n + 1))
#     # res.append(f(s1, s2 * 2, n + 1))
#     res.append(f(s1 + 1, s2))
#     res.append(f(s1 + s2, s2))
#     res.append(f(s1, s2 + 1))
#     res.append(f(s1, s2 + s1))
#     win = []
#     lose = []
#     for move in res:
#         if move[0] == '-':
#             win.append(move[1])
#         else:
#             lose.append(move[1])
#     # if n == 1 and lose: #Петя делает очень плохой ход. Если есть хотя бы один прооигрывающий ход
#     #     return ['-', min(lose)] #и стремиться проиграть как можно быстрее, для ?19
#     if win:
#         return ['+', min(win) + 1]
#     return ['-', max(lose)]
#
# for s in range(1,54):
#     # print(s, f(5, s, 1)) #для ?19
#     print(s, f(11, s))

import functools
@functools.cache

def f(s1, s2):
    if s1 + s2 >= 61:
        return ['-', 0]
    res = []
    res.append(f(s1 + 1, s2))
    res.append(f(s1, s2 * 2))
    res.append(f(s1 * 2, s2))
    res.append(f(s1, s2 * 2))
    win = []
    lose = []
    for move in res:
        if move[0] == '-':
            win.append(move[1])
        else:
            lose.append(move[1])

    if win:
        return ['+', min(win) + 1]
    return ['-', max(lose)]
print(f(5, 27))
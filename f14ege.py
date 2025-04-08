for x in range(1, 10000):
    y = 216 ** 8 + 36 ** 2 - x
    s = ""
    while y != 0:
        s += str(y % 6)
        y //= 6
    s = s[::-1]
    if s.count("5") == 20:
        print(x)
        break
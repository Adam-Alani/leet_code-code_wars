def last_digit(lst):
    c = 0
    res = 1
    for i in range(len(lst) - 1, -1, -1):
        if res == 0:
            res = 1
        elif res == 1:
            res = lst[i]
        else:
            res = lst[i] ** (res % 4 + 4)
    return res % 10


print(last_digit([937640, 767456, 981242]))

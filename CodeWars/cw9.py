def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19, 11 * 11]
print((comp(a1, a2)))

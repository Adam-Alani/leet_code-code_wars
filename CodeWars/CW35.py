def next_smaller(n):
    array = list(str(n))
    lngth = len(array)
    try:
        pv = next(i for i in reversed(range(lngth-1)) if array[i] > array[i+1])
        sw = next(i for i in reversed(range(lngth)) if array[pv] > array[i])
        array[pv],array[sw] = array[sw],array[pv]
        array[pv+1:] = reversed(array[pv+1:])
        if array[0] == '0':
            return -1
        else:
            print(int(''.join(d for d in array)))
    except StopIteration:
        print(-1)

next_smaller(1027)
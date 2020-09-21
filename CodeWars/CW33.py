def next_bigger(n):
    array = list(str(n))
    length = len(array)
    i = next(i for i in reversed(range(length-1)) if array[i] < array[i+1])
    j = next(i for i in reversed(range(length)) if array[i] < array[i])
    array[i],array[j] = array[j],array[i]
    array[i+1:] = reversed(array[i+1:])
    return int(''.join(d for d in array))


print(next_bigger(2017))
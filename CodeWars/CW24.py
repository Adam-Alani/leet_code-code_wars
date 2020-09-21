def move_zeros(array):
    array.sort(key=lambda item: item == 0 and not isinstance(item, bool))
    return(array)
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))

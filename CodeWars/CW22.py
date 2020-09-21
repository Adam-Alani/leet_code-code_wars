def spinning_rings(inner_max, outer_max):
    inner = inner_max
    outer = 1
    c = 0
    while inner != outer:
        outer += 1
        inner -= 1
        if outer > outer_max:
            outer = 0
        if inner < 0:
            inner = inner_max
        c += 1
    print(c+1)


print((spinning_rings(2**24, 3**15)))
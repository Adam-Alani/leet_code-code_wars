def dbl_linear(n):
    u = [1]
    x,y = 0,0
    for i in range(n):
        a = ((2 * u[x]) + 1)
        b = ((3 * u[y]) + 1)
        if a < b:
            u.append(a)
            x += 1
        elif b < a:
            u.append(b)
            y += 1
        else:
            u.append(a)
            x += 1
            y += 1
    print(u[n])



dbl_linear(471)
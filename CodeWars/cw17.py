def exp_sum(n):
    p,k = 0, 1
    if n == 0: p = 1
    elif n in cache: return(cache[n])
    else:
        while (n >= k):
            p1, p2 = (k * (3 * k - 1) / 2), (k * (3 * k + 1) / 2)
            p += (-1)**(k+1) * (exp_sum(n - p1) + exp_sum(n - p2))
            cache[n] = p
            k += 1
    return(p)
cache = {}



print(exp_sum(100))

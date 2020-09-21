def fib(n):
    res = 0
    if n == 0: return 0
    if n == 1: return 1
    elif n in cache: return (cache[n])
    if n <= -1:
        return (-1) ** (n + 1) * (fib(-n))
    else:
        res = fib(n-1) + fib(n-2)
        cache[n] = res
    return(res)
cache = {}


#fib(n) = fib(n-1) + fib(n-2)

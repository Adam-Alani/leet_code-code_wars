def digital_root(n):
    n = str(n)
    if len(n) == 1:
        return n
    else:
        total = 0
        for digit in (n):
            total += int(digit)
        n = str(total)
        return(digital_root(n))


print(int(digital_root(0)))
def countBits(n):
    bits, one = '{0:b}'.format(n), 0
    for digit in str(bits):
        one += int(digit)
    return(one)







print((countBits(4)))
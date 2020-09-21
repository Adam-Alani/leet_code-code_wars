def accum(s):
    res = []
    for count, letter in enumerate(s):
        res.append(letter.upper() + letter.lower() * (count))
    return '-'.join(res)



print((accum("ZpglnRxqenU")))
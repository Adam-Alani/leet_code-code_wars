import itertools
def permutations(string):
    temp = [''.join(p) for p in itertools.permutations(string)]
    return list(set(temp))




print(permutations('aa'))

import collections


def find_it(seq):
    if (len(seq)) == 1 : return(seq[0])
    seq = sorted(seq)
    temp = []
    for i in range(len(seq)):
        if seq[i] != seq[i-1]: temp.append(seq[i])
    for i in temp:
        if seq.count(i) % 2 != 0: return(i)




print(find_it([0]))

def wordPattern(pattern,str):
    res = str.split()
    return list(map(pattern.find, pattern)) == list(map(res.index , res))

print(wordPattern("abba","dog cat cat dog" ))
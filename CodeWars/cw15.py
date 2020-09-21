def who_is_next(names, r):
    while r <= len(names):
        return(names[r-1])
    while r >= len(names):
         r = ((r - len(names)+1) / 2)
    return(names[int(r)-1])


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
print((who_is_next(names,52)))



def sum_of_digits(a, b):
    temp = a
    for i in range(b-a):
        temp += a
        a += 1
        print(a)
    return temp







print(sum_of_digits(1,20))
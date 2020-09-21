def solution(number):
    mult3 = []
    mult5 = []
    for i in range(number):
        if 3 * i <= number-1:
            mult3.append(3*i)
        if 5 * i <= number-1:
            mult5.append(5*i)
    for item in mult5:
        for item2 in mult3:
            if item == item2:
                mult5.remove(item)

    total = sum(mult3) + sum(mult5)

    print(total)
    print(mult3)
    print(mult5)

print(solution(16))


def is_interesting(number, awesome_phrases):
    if number in awesome_phrases: return
    if number + 1 in awesome_phrases or number + 2 in awesome_phrases: return 1
    if mileage(number): return 2
    if mileage(number + 1) or mileage(number + 2): return 1
    return 0


def mileage(number):
    num = str(number)
    l = list(num)
    l = [int(i) for i in list(num)]

    if number <= 99: return False
    for i in range(len(num)):
        if number % 100 == 0:
            return True
        if all(elem == num[0] for elem in num):
            return True
        if num in '1234567890':
            return True
        if num in '9876543210':
            return True
        if num[::-1] == num:
            return True
    return False


print(is_interesting(12312321, (1337, 256)))

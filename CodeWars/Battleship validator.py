def validate_battlefield(field):
    BS = DS = CS = SM = c = sum1 = row = col = 0
    while c < 10:
        for i in range(10):
            if field[c][i] + field[c][i - 1] + field[c][i - 2] + field[c][i - 3] == 4:
                BS += 1
                field[c][i] = field[c][i - 1] = field[c][i - 2] = field[c][i - 3] = 0
            if field[i][c] + field[i - 1][c] + field[i - 2][c] + field[i - 3][c] == 4:
                BS += 1
                field[i][c] = field[i - 1][c] = field[i - 2][c] = field[i - 3][c] = 0
        c += 1
    c = 0
    while c < 10:
        for i in range(10):
            if field[c][i] + field[c][i - 1] + field[c][i - 2] == 3:
                CS += 1
                field[c][i] = field[c][i - 1] = field[c][i - 2] = 0
            if field[i][c] + field[i - 1][c] + field[i - 2][c] == 3:
                CS += 1
                field[i][c] = field[i - 1][c] = field[i - 2][c] = 0
        c += 1
    c = 0
    while c < 10:
        for i in range(10):
            if field[c][i] + field[c][i - 1] == 2:
                DS += 1
                field[c][i] = field[c][i - 1] = 0
            if field[i][c] + field[i - 1][c] == 2:
                DS += 1
                field[i][c] = field[i - 1][c] = 0
        c += 1
    c = 0
    while c < 10:
        for i in range(10):
            if field[c][i] == 1:
                SM += 1
                field[c][i] = 0
            if field[i][c] == 2:
                SM += 1
                field[i][c] = 0
        c += 1
    for i in range(10):
        for j in range(10):
            sum1 = sum1 + field[i][j]

    if BS == 1 and CS == 2 and DS == 3 and SM == 4 and sum1 == 0:
        return True

    else:
        return False




battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(validate_battlefield(battleField))
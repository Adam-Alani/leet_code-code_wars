def valid_solution(board):
    for i in range(len(board)):
        x = 0
        y = 0
        for j in range(len(board)):
            x += board[i][j]
            y += board[j][i]
        if board[i][j] < 1 or board[i][j] > 9:
            return(False)
        if x != 45 or y != 45:
            return(False)
    for i in range(3):
        for j in range(3):
            gadd = 0
            for k in range(3):
                for l in range(3):
                    gadd += board[i * 3 + k][j * 3 + l]
                    if board[i][j] < 1 or board[i][j] > 9:
                        print(3)
                        return(False)
            if gadd != 45:
                return(False)
            else:
                return(True)






print((valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]])))

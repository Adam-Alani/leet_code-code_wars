import copy
from itertools import permutations

def createBoard(n):
    board = [[[1, 2, 3, 4] for line in range(n)] for row in range(n)]
    return board

def solve_puzzle(clues):
    n = 4
    board = createBoard(n)
    fillInit(clues, board, n)
    constraintPropagation(board, n)
    recElim(board, n)
    convert_to_0(board)
    solve(board, clues)
    return tuple(tuple(sub) for sub in board)

def convert_to_0(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if isinstance(board[i][j], list):
                board[i][j] = 0
    return board

def getCells(i, board, n):
    if i < n:
        return [row[i] for row in board]  # Returns the Column from Top to Bottom
    if n <= i < 2 * n:
        return board[i - n][::-1]  # Returns the Row from Right to Left
    if 2 * n <= i < 3 * n:
        return [row[3 * n - i - 1] for row in board[::-1]]  # Returns the Column from Bottom to Top
    if 3 * n <= i < 4 * n:
        return board[4 * n - i - 1]  # Returns the Column from Left to Right

def putCells(i, board, n, elem):
    if i < n:
        for k in range(len(board)):
            board[k][i] = elem[k]
        return board

    if n <= i < 2 * n:
        board[i - n] = elem[::-1]
        return board

    if 2 * n <= i < 3 * n:
        for k in range(len(board)):
            board[k][3 * n - i - 1] = elem[::-1][k]
        return board

    if 3 * n <= i < 4 * n:
        board[4 * n - i - 1] = elem
        return board
    pass


def fillInit(clues, board, n):  # Modify
    for i in range(len(clues)):
        if 1 < clues[i] < n:
            try:
                cell = getCells(i, board, n)
                for d in range(len(cell)):
                    cell = getCells(i, board, n)
                    min = n - clues[i] + 2 + d
                    if min <= 4:
                        cell[d] = [x for x in cell[d] if x < min]
                        putCells(i, board, n, cell)
            except TypeError:
                pass
        if clues[i] == 1:
            cell = getCells(i, board, n)
            cell[0] = 4
            putCells(i, board, n, cell)

        if clues[i] == 4:
            cell = getCells(i, board, n)
            num = 1
            for d in range(len(cell)):
                cell[d] = num
                num += 1
            putCells(i, board, n, cell)
    return board

def constraintPropagation(board, n):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] in [1, 2, 3, 4]:
                checkCol(board, n, i, j)
                checkRow(board, n, i, j)
    recConstraint(board, n)
    return board


def recConstraint(board, n):
    for i in range(len(board)):
        for j in range(len(board)):
            if isinstance(board[i][j], list):
                if len(board[i][j]) == 1:
                    board[i][j] = board[i][j][0]
                    checkRow(board, n, i, j)
                    checkCol(board, n, i, j)
                    recConstraint(board, n)
    return board
def checkRow(board, n, i, j):
    valueElim = board[i][j]
    for k in range(len(board)):
        if isinstance(board[i][k], list):
            if valueElim in board[i][k]:
                board[i][k].remove(valueElim)
    return board

def checkCol(board, n, i, j):
    valueElim = board[i][j]
    for k in range(len(board)):
        if isinstance(board[k][j], list):
            if valueElim in board[k][j]:
                board[k][j].remove(valueElim)
    return board

def eliminateRow(board, n, rowIndex, colIndex):
    deleteVal = board[rowIndex][colIndex]
    compareVal = board[rowIndex]
    listcount = 0
    for i in range(len(compareVal)):
        if isinstance(compareVal[i], list):
            listcount += 1
    for i in range(len(deleteVal)):
        dist = 0
        for index, value in enumerate(compareVal, start=1):
            if isinstance(value, list):
                if index not in [colIndex + 1]:
                    if deleteVal[i] not in value:
                        dist += 1
                        if dist == listcount - 1:
                            board[rowIndex][colIndex] = deleteVal[i]
    return board


def eliminateCol(board, n, rowIndex, colIndex):
    deleteVal = board[rowIndex][colIndex]
    compareVal = [row[rowIndex] for row in board]
    listcount = 0
    for i in range(len(compareVal)):
        if isinstance(compareVal[i], list):
            listcount += 1
    for i in range(len(deleteVal)):
        dist = 0
        for index, value in enumerate(compareVal, start=1):
            if isinstance(value, list):
                if index not in [rowIndex + 1]:
                    if deleteVal[i] not in value:
                        dist += 1
                        if dist == listcount - 1:
                            board[rowIndex][colIndex] = deleteVal[i]
    return board

def recElim(board, n):
    new_board = 0
    while new_board != board:
        for i in range(len(board)):
            for j in range(len(board)):
                constraintPropagation(board, n)
                if isinstance(board[i][j], list):
                    eliminateRow(board, n, i, j)
                    new_board = board
        for i in range(len(board)):
            for j in range(len(board)):
                constraintPropagation(board, n)
                if isinstance(board[i][j], list):
                    eliminateCol(board, n, i, j)
                    new_board = board
    return board

def checkSkyscraper(seq):
    vis = max = 0
    for i in range(len(seq)):
        if seq[i] > max:
            vis += 1
            max = seq[i]
    return vis

def verifyDistance(cell):
    visible = 0
    max = 0
    for i in range(len(cell)):
        if cell[i] > max:
            visible += 1
            max = cell[i]
    return visible

def is_valid_solution(board, clues, n, num, pos):
    row = [num if i == pos[1] else board[pos[0]][i] for i in range(4)]
    col = [num if i == pos[0] else board[i][pos[1]] for i in range(4)]

    if row.count(num) > 1:
        return False
    if col.count(num) > 1:
        return False

    clue = clues[pos[1]]
    if clue != 0 and clue not in flatten(col):
        return False

    clue = clues[pos[0] + 4]
    if clue != 0 and clue not in flatten(row[::-1]):
        return False

    clue = clues[::-1][pos[1] + 4]
    if clue != 0 and clue not in flatten(col[::-1]):
        return False

    clue = clues[::-1][pos[0]]
    if clue != 0 and clue not in flatten(row):
        return False

    return True

def flatten(incompleted_row):
    possible_rows = []
    d = list({1, 2, 3, 4} - set([x for x in incompleted_row if x != 0]))
    for perm in permutations(d):
        row = incompleted_row.copy()
        for e in perm:
            row[row.index(0)] = e
        possible_rows.append(row)
    possible_clues = set()
    for r in possible_rows:
        possible_clues.add(verifyDistance(r))
    return list(possible_clues)

def solve(board, clues):
    find = empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 5):
        if is_valid_solution(board, clues, 4, i, (row, col)):
            board[row][col] = i
            if solve(board, clues): return True
            board[row][col] = 0
    return False

def empty(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0: return (i, j)
    return None

clues = ( 3, 2, 2, 3, 2, 1,
          1, 2, 3, 3, 2, 2,
          5, 1, 2, 2, 4, 3,
          3, 2, 1, 2, 2, 4)

print(solve_puzzle(clues))
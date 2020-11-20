import copy
from itertools import product
from itertools import permutations
from itertools import chain

def createBoard(n):
    board = [[[1, 2, 3, 4, 5, 6] for line in range(n)] for row in range(n)]
    return board

def convert_to_0(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if isinstance(board[i][j], list):
                board[i][j] = 0
    return board

def solve_puzzle(clues):
    n = 6
    board = createBoard(n)
    initial_clues(board, clues, n)
    constraintPropagation(board, n)
    board = recElim(board, n)
    zero = copy.deepcopy(board)
    zero = (convert_to_0(zero))
    search2(zero, clues, board)
    return zero
    # return tuple(tuple(sub) for sub in board)

def initial_clues(grid, clues, n):
    for i in range(len(grid)):
        if 1 < clues[i] < n:
            try:
                for j in range(n):
                    min = n - clues[i] + 2 + j
                    if min <= 6:
                        grid[j][i] = [x for x in grid[j][i] if x < min]
            except Exception:
                break
        if 1 < clues[i + n] < n:
            try:
                for j in range(n):
                    min = n - clues[i + n] + 2 + j
                    if min <= 6:
                        grid[i][n - 1 - j] = [x for x in grid[i][n - 1 - j] if x < min]
            except Exception:
                break
        if 1 < clues[3 * n - 1 - i] < n:
            try:
                for j in range(n):
                    min = n - clues[3 * n - 1 - i] + 2 + j
                    if min <= 6:
                        grid[n - 1 - j][i] = [x for x in grid[n - 1 - j][i] if x < min]
            except Exception:
                break
        if 1 < clues[4 * n - 1 - i] < n:
            try:
                for j in range(n):
                    min = n - clues[4 * n - 1 - i] + 2 + j
                    if min <= 6:
                        grid[i][j] = [x for x in grid[i][j] if x < min]
            except Exception:
                break

        if clues[i] == 1:
            grid[0][i] = n
        if clues[i + n] == 1:
            grid[i][-1] = n
        if clues[3 * n - 1 - i] == 1:
            grid[-1][i] = n
        if clues[4 * n - 1 - i] == 1:
            grid[i][0] = n

        if clues[i] == n:
            for j in range(n):
                grid[j][i] = j + 1
        if clues[i + n] == n:
            for j in range(n):
                grid[i][n - 1 - j] = j + 1
        if clues[3 * n - 1 - i] == n:
            for j in range(n):
                grid[n - 1 - j][i] = j + 1
        if clues[4 * n - 1 - i] == n:
            for j in range(n):
                grid[i][j] = j + 1
    return grid

def constraintPropagation(board, n):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] in [1, 2, 3, 4, 5, 6]:
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
    try:
        for i in range(len(deleteVal)):
            dist = 0
            for index, value in enumerate(compareVal, start=1):
                if isinstance(value, list):
                    if index not in [colIndex + 1]:
                        if deleteVal[i] not in value:
                            dist += 1
                            if dist == listcount - 1:
                                board[rowIndex][colIndex] = deleteVal[i]
    except Exception:
        pass
    return board

def eliminateCol(board, n, colIndex, rowIndex):
    deleteVal = board[rowIndex][colIndex]
    compareVal = [row[colIndex] for row in board]

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

temp = []
def recElim(board, n):
    while True:
        for i in range(len(board)):
            for j in range(len(board)):
                constraintPropagation(board, n)
                if isinstance(board[i][j], list):
                    eliminateRow(board, n, i, j)
        for i in range(len(board)):
            for j in range(len(board)):
                constraintPropagation(board, n)
                if isinstance(board[j][i], list):
                    board = (eliminateCol(board, n, i, j))
        if board in temp:
            return board
        temp.append(board)
        return board

def verifyDistance(cell):
    visible = 0
    max = 0
    for i in range(len(cell)):
        if cell[i] > max:
            visible += 1
            max = cell[i]
    return visible

def flatten(incompleted_row):
    possible_rows = []
    d = list({1, 2, 3, 4, 5, 6} - set([x for x in incompleted_row if x != 0]))
    for perm in permutations(d):
        row = incompleted_row.copy()
        for e in perm:
            row[row.index(0)] = e
        possible_rows.append(row)
    possible_clues = set()
    for r in possible_rows:
        possible_clues.add(verifyDistance(r))
    return list(possible_clues)

def empty(puzzle):
    if 0 in chain.from_iterable(puzzle):
        return True
    return None

def search(zero, clues, searchBoard):
    find = empty(zero)    #Checks for zeroes in a duplicate list
    findLeast = full(searchBoard)  #Checks for elements that have more than one possibility
    if not find :
        return True
    else:
        row , col = findLeast  #Fetches the index of the element with least amount of possibilities
    val = searchBoard[row][col]
    for i in searchBoard[row][col]:   #loops through those possibilties
        if is_valid_solution(zero, clues, 6, i, (row, col)):
            zero[row][col] = i    #If the possibilitie works, insert it
            searchBoard[row][col] = i
            if search(zero, clues, searchBoard):   #recursively do this (backtrack) until no more empty elements in the zeroes duplicate list
                return True
            zero[row][col] = 0         #else: reset, try again for different values
            searchBoard[row][col] = val
    return False

def search2(zero, clues, searchBoard):
    find = full(searchBoard)
    while find :
        print(searchBoard)
        find = empty(zero)  # Checks for zeroes in a duplicate list
        findLeast = full(searchBoard)  # Checks for elements that have more than one possibility
        row , col = findLeast  #Fetches the index of the element with least amount of possibilities
        val = searchBoard[row][col]
        for i in searchBoard[row][col]:   #loops through those possibilties
            if is_valid_solution(zero, clues, 6, i, (row, col)):
                zero[row][col] = i    #If the possibilitie works, insert it
                searchBoard[row][col] = i
            else:
                zero[row][col] = 0         #else: reset, try again for different values
                searchBoard[row][col] = val
    return zero

def full(puzzle):

    pos = []

    for i in range(len(puzzle)):   #loop through the rows of the puzzle
        try:
            pos.append([( i ,puzzle[i].index(min((x for x in puzzle[i] if isinstance(x,list)),key=len))) , puzzle[i] ])
            # append the tuple (i , j) where i is the row number and j the column number, and the smallest list of possibilities in each row
        except ValueError:
            i +=1

    try:
        champion, champion_len = pos[0][0], len(pos[0][1])  #unpack the pos list into the tuple, and the possibilties
    except IndexError:
        return None
    for t, sl in pos:
        if len(sl) < champion_len:
            champion, champion_len = t, len(sl)   #look for the smallest number of possibilities and return their index
    return champion

def is_valid_solution(board, clues, n, num, pos):
    row = [num if i == pos[1] else board[pos[0]][i] for i in range(6)]
    col = [num if i == pos[0] else board[i][pos[1]] for i in range(6)]

    if row.count(num) > 1:
        return False
    if col.count(num) > 1:
        return False

    clue = clues[pos[1]]
    if clue != 0 and clue not in flatten(col):
        return False

    clue = clues[pos[0] + 6]
    if clue != 0 and clue not in flatten(row[::-1]):
        return False

    clue = clues[::-1][pos[1] + 6]
    if clue != 0 and clue not in flatten(col[::-1]):
        return False

    clue = clues[::-1][pos[0]]
    if clue != 0 and clue not in flatten(row):
        return False
    return True





clues = ( 3, 2, 2, 3, 2, 1,
          1, 2, 3, 3, 2, 2,
          5, 1, 2, 2, 4, 3,
          3, 2, 1, 2, 2, 4)


# print(test(createBoard(6), clues))

def print_board(bo):
    for i in range(len(bo)):
        if i % 1 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 1 == 0 and j != 0:
                print(" | ", end="")

            if j == 5:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

print_board((solve_puzzle(clues)))

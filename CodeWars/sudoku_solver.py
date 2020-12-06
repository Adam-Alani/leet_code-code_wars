
def empty(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0: return(i, j)
    return None
    pass

def valid(puzzle, num, pos):
    for i in range(len(puzzle[0])):
        if puzzle[pos[0]][i] == num and pos[1] != i:
            return False
        if puzzle[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if puzzle[i][j] == num and (i,j) != pos:  return False
    return True
    pass

def solve(puzzle):
    find = empty(puzzle)
    if not find: return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(puzzle, i, (row, col)):
            puzzle[row][col] = i
            if solve(puzzle): return True
            puzzle[row][col] = 0
    return False
    pass

def sudoku(puzzle):
    solve(puzzle)
    return puzzle






puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,0,0,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

(sudoku(puzzle))


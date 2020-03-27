# A backtracking algorithm that solves sudoku puzzles

# find a unassigned cell (rol,col) and try fill it in with 1-9
# check is same number is in the same rol or col and subgrid
# if the nubmer fails, we try the next available number in the current unassigned cell
# if there is no solution for current cell, backtrack to the previous cell
# recursively do this until we reach a solution
# return false if there is no solution to the puzzle (recursion fails)


# this is the temporary board
# we will change this when we write program to generate sudoku board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# displaying the board with empty slots and subgrids
def printBoard(board):
    # i is the row num
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - -")

        #j is the col num
        for j in range(len(board[i])):
            if j%3==0 and j!=0:
                print(" | ", end='')
            if j==8:
                print(board[i][j])
            else:
                print(board[i][j], end=' ')

# this function finds an unassigned cell
def findempty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i,j) #rol, col
    return None

# this checks if the number is safe to assign
# checks rol, col and subgrid
def valid(board, num, pos):
    #checks row
    for i in range(9):
        #if the num exists in the row and it is not the pos we are accessing right now
        if board[pos[0]][i] == num and pos[1] != i: 
            return False

    #checks column
    for j in range(9):
        if board[j][pos[1]] == num and pos[0] != j:
            return False
    
    #checks subgrid
    subgrid_x = pos[1] // 3 #finds subgrid coordinates
    subgrid_y = pos[0] // 3
    
    for i in range(subgrid_y*3, subgrid_y*3 + 3):
        for j in range(subgrid_x*3, subgrid_x*3 + 3):
            if num == board[i][j] and (i,j) != pos:
                return False

    #if the number is safe
    return True

def solve(board):
    empty = findempty(board)
    if not empty:
        return True
    row, col  = empty
    # testing number between 1-9
    for i in range(1,10):
        if valid(board, i, (row,col)):
            #if the number is safe to assign, then assign it to empty cell
            board[row][col] = i
            #recursion, if success, then true unique solution
            if solve(board):
                return True
            #if recursion fails, reset the previous empty cell and try another number
            board[row][col] = 0
    return False
            
printBoard(board)
print("==========================")
print(solve(board))


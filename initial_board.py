# this is code i pulled from 
# https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
# this generates a full board, and then removes numbers from the board

from random import sample

base  = 3
side  = base*base 

# pattern for a baseline valid solution
def pattern(r,c): 
    return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): 
    return sample(s,len(s)) 

def initial_board():
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    return board

def board_removed_numbers():
    board = initial_board()

    squares = side*side
    empties = squares * 3//4
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0

    board_ready = []
    for line in board:
        board_ready.append(line)
    return board_ready
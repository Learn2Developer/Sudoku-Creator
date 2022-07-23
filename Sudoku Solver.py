from random import sample
board = []
game_still_going = True
square = []
col = []
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""So we need to make the logic for making the 2D grid, then create a board for the game, 
then, given a board state, how does the game know which squares to fill in?"""

def print_board(board):

def make_board():
    x = 0
    while x < 9:
        board.append(sample(num_list, 9))
        x += 1

def check_row(row):
    while "123456789" not in row:
        #row not complete
        pass

def check_square(square):
    while "123456789" not in square:
        #square not complete    
        pass

def check_col(col):
    while "12345789" not in col:
        #col not complete
        #possibly check for columns by zipping lists and checking that each index contains 1-9.
        pass

make_board()
print_board(board)
print(sample(num_list, 9))
import random
board = []
game_still_going = True
square = []
col = []

"""So we need to make the logic for making the 2D grid, then create a board for the game, 
then, given a board state, how does the game know which squares to fill in?"""


for each in range(0, 9):
    board.append("x" * 9)

def print_board(board):
    x = 0
    for i in board:
        print("|" + "|".join(i) + "|")
        x += 1
        if x % 3 == 0:
            print("___________________")

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
        pass


print_board(board)

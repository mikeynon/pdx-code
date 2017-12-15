
# CONNECT FOUR
#
# LAB: CONNECT FOUR
#
# Connect Four is a board game.
# Players take turns placing tokens of their color into a vertical grid.
# They drop to the bottom, and if anyone has four of their color in a straight line, they’ve won!
#
# Create a program that simulates the just playing moves of an existing Connect Four game.
# Do not concern yourself with figuring out who has won.
#
# It will read a file that contains a history of the moves in a game.
# Assume the playing board is made of columns numbered 1 through 7.
# The file will have one line for each move (players alternate).
# The number in that line is the column the current player placed a token in.
#
# Use the following to create a new file called connect-four-moves.txt
# This moves file recreates this game.
#
# Think about how to figure out how far that token will fall in a given column.
#
# Think about how to place a token in a column.
#
# Think about how to concisely store the tokens that have been dropped in the board.
#
# Read in moves from the file.
#
# After each move, print out a representation of the board.
# You can use R and Y to represent the pieces.
#
# ADVANCED
#
# Once all moves are done, also print out what player, if any, won.

# def boardLogic(pick, user):
import numpy as np
import pygame
import sys
# user_1 = "R"
# user_2 = "Y"
pygame.init()
SQUARESIZE = 110
RADIUS = int((SQUARESIZE/2)-5)
width = col_count * SQUARESIZE
height = SQUARESIZE * (row_count+1)
size= (width, height)
screen = pygame.display.set_mode(size)
game_over = False
turn = 0
blue = (0,0,255)
yellow = (0,255,0)
red = (255,0,0)
black = (0,0,0)
row_count = 6
col_count = 7
# columns = range(1,7+1)
# rows = range(1,7+1)
# moves = {
# R to 4, Y to 3, R to 5, Y to 6,
# R to 4, Y to 4, R to 5, Y to 3,
# R to 6, Y to 2, R to 7, Y to 3, R to 3,
# Y to 7, R to 4, Y to 5, R to 6, Y to 5
# }
# win if four in a row
# players alternate turns
def create_board(board):
    board = np.zeros((row_count,col_count))
    return board
def drop_piece(board, row, col, piece):
    board[row][col]= piece
def valid_spot(board, col):
    return board[row_count-1][col] == 0
def next_open_row(board, col):
    for r in range(row_count):
        if board [r][col] == 0:
            return [r]
def print_board(board):
    print(np.flip(board, 0))
def draw_board(board):
    for c in range(col_count):
        for r in range(row_count):
            pygame.draw.rect(screen, blue, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, black, (int(c * SQUARESIZE+SQUARESIZE/2), (int(r * SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS))
        continue
def winning_move(board, piece):
    for c in range(col_count-3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2]==piece and board[r][c+3] == piece:
                return True
    for c in range(col_count):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c]==piece and board[r+3][c] == piece:
                return True
    for c in range(col_count-3):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2]==piece and board[r+3][c+3] == piece:
                return True
    for c in range(col_count+3):
        for r in range(3, row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2]==piece and board[r-3][c+3] == piece:
                return True
board = create_board
print_board(board)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
             if turn ==0:
                col = int(input("Where would you like to drop the piece (0-6):\n"))
                if valid_spot(board, col):
                    row = next_open_row[board][col]
                    drop_piece(board, row, col, 1)
                if winning_move(board, 1):
                    print("Player 1 Wins")
                    game_over == True
        else:
            col = int(input("Where would player 2 like to drop the piece (0-6ß):\n"))
            if valid_spot(board, col):
                row = next_open_row[board][col]
                drop_piece(board, row, col, 2)
            if winning_move(board, 2):
                print("Player 2 Wins")
                game_over == True
        print_board(board)
        turn += 1
        turn = turn%2

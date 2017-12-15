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
import Numpy
import random
user_1 = "R"
user_2 = "Y"

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

def board():
    board = np.zeroes(6,7)
    return board

def drop_piece():
    pass
def valid_spot():
    pass

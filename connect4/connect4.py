import numpy as np


def create_board():
    board = np.zeros((6, 7))
    return board


board = create_board()
game_over = False
turn = 0

while not game_over:
    # ask for player1 input
    if turn == 0:
        selection = int(input("Player1 - make your selection (0-6): "))
    else:
        selection = int(input("Player2 - make your selection (0-6): "))
    turn += 1
    turn = turn % 2

import pygame
from Constants import *

'''
    Rules of Tic Tac Toe
    Rule 1: the game is played on a 3x3 grid
    Rule 2: there are 2 players "x" and "o"
    Rule 3: They take turns placing their mark in one
        of the squares of the board
    Rule 4: The first Player to get 3 in a row
        column or diagonal wins the game

    By: Jason Sykes
'''


def build_board(ttt):
    background = pygame.Surface(ttt.get_size())
    background = background.convert()
    background.fill((250, 250, 250))


def change_player(game_player):
    return (+1 if game_player == -1 else -1)


def choose_square(x, y, game_player):
    if (-1 < x < 3 and -1 < y < 3
            and game_board[x][y] == 0):
        game_board[x][y] = game_player
        # change_player(game_player)
    else:
        print("Position Not available\n")


def is_game_over(board_state, game_player):
    if (any(0 in sublist for sublist in board_state)):
        for row in range(0, 3):
            if ((board_state[row][0] ==
                 board_state[row][1] ==
                 board_state[row][2] and
                 (board_state[row][0] is not 0))):
                print("1Winner is: " + ("X" if game_player == -1 else "O"))
                return True

        for col in range(0, 3):
            if ((board_state[0][col] ==
                 board_state[1][col] ==
                 board_state[2][col] and
                 (board_state[0][col] is not 0))):
                print("2Winner is: " + ("X" if game_player == -1 else "O"))
                return True

        # checking for the diagonals
        if (board_state[0][0] ==
                board_state[1][1] ==
                board_state[2][2] and
                board_state[0][0] is not 0):
            print("3Winner is " + ("X" if game_player == -1 else "O"))
            return True

        if (board_state[0][2] ==
                board_state[1][1] ==
                board_state[2][0] and
                board_state[0][2] is not 0):
            print("4Winner is " + ("X" if game_player == -1 else "O"))
            return True
        print("Game can continue")
        return False

    else:
        print("Game is a Draw")
        return True


def boardPos(mouseX, mouseY):
    if (mouseX < 100):
        row = 0
    elif (mouseX < 200):
        row = 1
    else:
        row = 2

    if (mouseY < 100):
        col = 0
    elif (mouseY < 200):
        col = 1
    else:
        col = 2

    return (row, col)


def print_game_board():
    for x in game_board:
        print(x)

import pygame
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
game_board = [[" "] * 3 for _ in range(3)]

def new_game():
    game_board = [[" "] * 3 for _ in range(3)]

def build_board(ttt):
    background = pygame.Surface(ttt.get_size())
    background = background.convert()
    background.fill((250,250,250))

def change_player(game_player):
    return ("O" if game_player == "X" else "X")

def choose_square(x,y,game_player):
    if(-1 < x < 3 and -1 < y < 3
            and game_board[x][y] == " "):
        game_board[x][y] = game_player
        # change_player(game_player)
    else:
        print("Position Not available\n")

def is_game_over(game_player):
    global game_board

    if(any(" " in sublist for sublist in game_board)):
        for row in range(0,3):
            if((game_board[row][0] ==
                game_board[row][1] ==
                game_board[row][2] and
                (game_board[row][0] is not " "))):
                print("1Winner is: " + game_player)
                return True

        for col in range(0,3):
            if((game_board[0][col] ==
                game_board[1][col] ==
                game_board[2][col] and
                (game_board[0][col] is not " "))):
                print("2Winner is: " + game_player)
                return True

        # checking for the diagonals
        if(game_board[0][0] ==
                game_board[1][1] ==
                game_board[2][2] and
                game_board[0][0] is not " "):
            print("3Winner is " + game_player)
            return True


        if (game_board[0][2] ==
                game_board[1][1] ==
                game_board[2][0] and
                game_board[0][2] is not " "):
            print("4Winner is " + game_player)
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

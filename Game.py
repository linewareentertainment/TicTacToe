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

game_player = "X"
game_over = False

game_board = [[" "] * 3 for _ in range(3)]

def build_board(ttt):
    background = pygame.Surface(ttt.get_size())
    background = background.convert()
    background.fill((250,250,250))
    That is all for now,  we will finish this up tomorrow
    see you then.  Going to leave this error here.
    If you want to see this code you can find it on my
    github at:
    https://github.com/linewareentertainment/TicTacToe

    and remember comment like and subscribe for more content
        have a great day

def change_player():
    global game_player
    game_player = ("O" if game_player == "X" else "X")

def choose_square(x,y):
    if(-1 < x < 3 and -1 < y < 3
            and game_board[x][y] == " "):
        game_board[x][y] = game_player
        is_game_over()
        change_player()
    else:
        print("Position Not available\n")

def is_game_over():
    global game_player, game_board, game_over

    if(any(" " in sublist for sublist in game_board)):
        for row in range(0,3):
            if((game_board[row][0] ==
                game_board[row][1] ==
                game_board[row][2] and
                (game_board[row][0] is not " "))):
                print("Winner is: " + game_player)
                game_over = True
                print_game_board()
                return

        for col in range(0,3):
            if((game_board[0][col] ==
                game_board[1][col] ==
                game_board[2][col] and
                (game_board[0][col] is not " "))):
                print("Winner is: " + game_player)
                game_over = True
                print_game_board()
                return

        # checking for the diagonals
        if(game_board[0][0] ==
                game_board[1][1] ==
                game_board[2][2] and
                game_board[0][2] is not " "):
            print("Winner is " + game_player)
            game_over = True
            print_game_board()
            return

        if (game_board[0][2] ==
                game_board[1][1] ==
                game_board[2][0] and
                game_board[0][2] is not " "):
            print("Winner is " + game_player)
            game_over = True
            print_game_board()
            return
        print("Game can continue")

    else:
        print("Game is a Draw")
        game_over = True

def print_game_board():
    for x in game_board:
        print(x)

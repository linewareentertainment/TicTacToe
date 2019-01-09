import pygame
from Constants import *
from GameScene import GameMechanics \
    as game, BoardGraphics

pygame.init()

'''
    Next time we are going to put the menu on the board.
    Also we are going to have the winner screen pop up
    instead of show at the bottom.
'''

#this is ttt
screen = pygame.display.set_mode((W_SIZE, H_SIZE))
board = BoardGraphics.drawBoard(screen)

game_player = "X"
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif game_over:
            continue
        elif event.type is pygame.MOUSEBUTTONDOWN:
            BoardGraphics.boardClick(board, game_player)
            game_over = game.is_game_over(game_player)
            if not game_over:
                game_player = game.change_player(game_player)

        BoardGraphics.showBoard(screen, board,
                                game_player, game_over)

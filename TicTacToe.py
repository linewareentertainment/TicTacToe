import pygame
from GameScene import GameMechanics \
    as game, BoardGraphics

pygame.init()

#this is ttt
screen = pygame.display.set_mode((300,325))
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

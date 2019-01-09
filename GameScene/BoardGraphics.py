import pygame
from GameScene import GameMechanics as game
from Constants import *

def drawBoard(ttt):
    background = pygame.Surface(ttt.get_size())
    background = background.convert()
    background.fill(COLOR_BACKGROUND)  #background color

    pygame.draw.line(background,    #surface
                     BOARD_COLOR,       #color
                     (100,0),       #start_pos
                     (100,300), 12)  #end_pos and width
    pygame.draw.line(background,
                     BOARD_COLOR,
                     (200,0),
                     (200,300), 12)


    pygame.draw.line(background,
                     BOARD_COLOR,
                     (0,100),
                     (300,100), 12)
    pygame.draw.line(background,
                     BOARD_COLOR,
                     (0, 200),
                     (300,200), 12)

    return background

def drawMove(board, row, col, game_player):
    centerX = ((row) * 100) + 50
    centerY = ((col) * 100) + 50

    if(game_player == "O"):
        pygame.draw.circle(board,
                           COLOR_BLACK,
                           (centerX, centerY),
                           34,
                           12)
    else:
        pygame.draw.line(board,
                         COLOR_BLACK,
                         (centerX - 22, centerY - 22),
                         (centerX + 22, centerY + 22),
                         12)
        pygame.draw.line(board,
                         COLOR_BLACK,
                         (centerX + 22, centerY - 22),
                         (centerX - 22, centerY + 22),
                         12)
    game.choose_square(row,col,game_player)


def boardClick(board, game_player):
    (mouseX,mouseY) = pygame.mouse.get_pos()
    (row, col) = game.boardPos(mouseX,mouseY)

    drawMove(board,row,col, game_player)

def drawStatus(board, message):
    font = pygame.font.Font(None, 24)
    text = font.render(message, 1, COLOR_WHITE)

    board.fill(MENU_BACKGROUND_COLOR,(0,300,300,25))
    board.blit(text, (board.get_rect().width/3,
                      board.get_rect().height - 20))

def showBoard(ttt, board, game_player, game_over):
    if game_over == True :
        drawStatus(board, "Winner is " + game_player)
    ttt.blit(board, (0,0))
    pygame.display.flip()


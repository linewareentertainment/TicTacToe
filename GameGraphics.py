import pygame
import Game as game

game_player = "X"

def drawBoard(ttt):
    background = pygame.Surface(ttt.get_size())
    background = background.convert()
    background.fill((100,250,250))  #background color

    pygame.draw.line(background,    #surface
                     (0,0,0),       #color
                     (100,0),       #start_pos
                     (100,300), 12)  #end_pos and width
    pygame.draw.line(background,
                     (0,0,0),
                     (200,0),
                     (200,300), 12)


    pygame.draw.line(background,
                     (0,0,0),
                     (0,100),
                     (300,100), 12)
    pygame.draw.line(background,
                     (0,0,0),
                     (0, 200),
                     (300,200), 12)

    return background

def boardPos(mouseX, mouseY):
    if(mouseX < 100):
        row = 0
    elif(mouseX < 200):
        row = 1
    else: row = 2

    if (mouseY < 100):
        col = 0
    elif (mouseY < 200):
        col = 1
    else:
        col = 2

    return (row, col)


def drawMove(board, row, col):
    global game_player
    centerX = ((row) * 100) + 50
    centerY = ((col) * 100) + 50

    if(game_player == "O"):
        pygame.draw.circle(board,
                           (0,0,0),
                           (centerX, centerY),
                           44,
                           12)
    else:
        pygame.draw.line(board,
                         (0,0,0),
                         (centerX - 22, centerY - 22),
                         (centerX + 22, centerY + 22),
                         12)
        pygame.draw.line(board,
                         (0,0,0),
                         (centerX + 22, centerY - 22),
                         (centerX - 22, centerY + 22),
                         12)
    game.choose_square(row,col,game_player)


def boardClick(board):
    global game_player
    (mouseX,mouseY) = pygame.mouse.get_pos()
    (row, col) = boardPos(mouseX,mouseY)

    drawMove(board,row,col)

    game_player = game.change_player(game_player)

def showBoard(ttt, board):
    ttt.blit(board, (0,0))
    pygame.display.flip()


import pygame
import Game as game

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

def drawMove(board, row, col, game_player):
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


def boardClick(board, game_player):
    (mouseX,mouseY) = pygame.mouse.get_pos()
    (row, col) = game.boardPos(mouseX,mouseY)

    drawMove(board,row,col, game_player)

def drawStatus(board, message):
    font = pygame.font.Font(None, 24)
    text = font.render(message, 1, (10,10,10))

    board.fill((250,250,250),(0,300,300,25))
    board.blit(text, (10,300))

def showBoard(ttt, board, game_player, game_over):
    drawStatus(board, "Winner is " + game_player
    if game_over == True else " ")
    ttt.blit(board, (0,0))
    pygame.display.flip()


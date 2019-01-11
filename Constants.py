from pygameMenu.locals import *

H_SIZE = 325
W_SIZE = 300

game_board = [[0] * 3 for _ in range(3)]
game_over = False

ABOUT = ['Author: {0}'.format("Jason Sykes"),
         PYGAMEMENU_TEXT_NEWLINE,
         'Youtube: {0}'.format("https://www.youtube.com/lineware")]

COLOR_BLACK = (23, 25, 27)
COLOR_WHITE = (241, 240, 238)
COLOR_BACKGROUND = (105, 222, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (51, 165, 255)
BOARD_COLOR = (255, 196, 56)
# this will need to change to the game size
WINDOW_SIZE = (W_SIZE, H_SIZE)

FONT_SIZE = 16
FONT_TITLE_SIZE = 30

import pygame, random

def main():

    pygame.init()
    pygame.display.set_caption("Hello Tic Tac Toe")
    image = pygame.image.load("/jmsykes15/PycharmProjects/Test/Elf_Rogue_Female09_SR.png")
    screen = pygame.display.set_mode((240,180))


    running = True
    while running:
        pygame.display.flip()
        screen.fill((125,200,125))
        screen.blit(image, (50, 50))

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT :
                running = False

class TicTacTow ():Test
    board = [' ',' ',' ',
             ' ',' ',' ',
             ' ',' ', ' ']
    random = random
    ended = False
    currentPlayer = 'X'

    def isEnded(self):
        return self.ended

    def play(self, x):
        if(not self.ended and self.board[x] == ' '):
            self.board[x] = self.currentPlayer
            self.checkEnd()
        return self.changePlayer()


    def changePlayer(self):
        self.currentPlayer = ('X' if self.currentPlayer == 'O' else 'O')

    def getBoard(self, x, y):
        return self.board[3*y+x]

    def newGame(self):
        for i in range(0, 9):
            self.board[i] = ' ';
        self.currentPlayer = 'X'
        self.ended = False

    def checkEnd(self):
        for i in range(0,3):
            if self.getBoard(i,0) != ' ' and \
                self.getBoard(i,0) == self.getBoard(i,1) and \
                self.getBoard(i,1) == self.getBoard(i,2):
                self.ended = True
                print("Player %s wins!!!" % self.currentPlayer)
                return self.getBoard(i, 0);

            if self.getBoard(0, i) != ' ' and \
                self.getBoard(0,i) == self.getBoard(1,i) and \
                self.getBoard(1,i) == self.getBoard(2,i):
                self.ended = True
                print("Player %s wins!!!" % self.currentPlayer)
                return self.getBoard(0, i);

        if self.getBoard(2, 0) != ' ' and \
            self.getBoard(2, 0) == self.getBoard(1, 1) and \
            self.getBoard(1, 1) == self.getBoard(0, 2):
            self.ended = True
            print("Player %s wins!!!" % self.currentPlayer)
            return self.getBoard(2, 0);

        if self.getBoard(0, 0) != ' ' and \
            self.getBoard(0, 0) == self.getBoard(1, 1) and \
            self.getBoard(1, 1) == self.getBoard(2, 2):
            self.ended = True
            print("Player %s wins!!!" % self.currentPlayer)
            return self.getBoard(0, 0);
        for i in range(0,9):
            if self.board[i] == ' ':
                return ' '
        return 'T'

    def computer(self):
        if(not self.ended):
            position = -1

            while not self.board[position] != ' ':
                position = random.randint(0, 8)

            self.board[position] == self.currentPlayer
            self.changePlayer()

        return self.checkEnd()

if __name__ == "__main__":
    main()

# tictactoe = TicTacTow()
#
# while True:
#     print("Please type the square you would like to choose:")
#     print(tictactoe.board[0:3])
#     print(tictactoe.board[3:6])
#     print(tictactoe.board[6:])
#     numby = input("Position: ")
#     if(str(numby) == "new game"):
#         tictactoe.newGame()
#     elif(numby == "exit"):
#         break
#     elif(numby in ["{:01d}".format(x) for x in range(0,9)]):
#         tictactoe.play(int(numby))
#         tictactoe.computer()
#     else:
#         print(numby)
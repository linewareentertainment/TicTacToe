import Game as game

while(not game.game_over):
    game.print_game_board()
    print("Choose a square "
          "or press exit to leave the game")
    player_input = input("-> ")
    if(player_input == "exit" or game.game_over == True):
        print("Have a good day!")
        break

    elif(len(list(player_input.split(" "))) != 2):
        print("Please try again. You want it to be "
              "n the format 'x y'")
    else:
        lst = list(player_input.split(" "))
        try:
            game.choose_square(int(lst[0]),int(lst[1]))
        except(ValueError):
            print("Choose a number 0 through 2 for x and y")


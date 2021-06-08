from Board import Board

board = Board()

# board.saveLoad = ''

board.toggleGameStatus(1)

# board.printPiles()
board.saveLoad = 'l'

while board.playing:
    # if board.saveLoad == 's':
    #     board.saveGame()
    #     break
    if board.winning_player != 0:
        if board.winning_player == 3:
            print("The game ended in draw!")
            break
        else:
            print("Congratulation Player ", board.winning_player, ", YOU WON!")
            break

    if board.saveLoad == 'l':
        board.loadGame()
        board.printPiles()
    print("Its Player ", board.player, " turn !")
    board.clicked_index = int(input("Please enter the starting index\n"))

    board.prepMove()
    board.printPiles()
    board.saveLoad = input("Do you wish to save?\n")










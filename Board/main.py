from Board import Board

board = Board()


board.toggleGameStatus(1)
board.printPiles()

while board.playing:

    if board.winning_player != 0:
        if board.winning_player == 3:
            print("The game ended in draw!")
            break
        else:
            print("Congratulation Player ", board.winning_player, ", YOU WON!")
            break

    print("Its Player ", board.player, " turn !")
    board.clicked_index = int(input("Please enter the starting index\n"))

    board.prepMove()
    board.printPiles()









from Board import Board



board= Board()

board.toggleGameStatus(1)

while(board.playing==True):

    if board.winning_player == 0:
        board.moveFromPile()
    elif board.winning_player == 1:
        print("Player 1 is the winner !")
        break
    elif board.winning_player == 2:
        print("Player 2 is the winner !")
        break
    else :
        print ("Draw ~0~")
        break



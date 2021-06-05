class Board:

    def __init__(self):
        self.playing = False
        self.player = 1
        # zero-stone piles are the store of each player.
        self.piles = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

    # Start or end and choose player 1 or 2 to start

    def toggleGameStatus(self):
        pass

    # if player 1 turn ends , it toggles to player 2.
    def togglePlayer(self):
        pass

    # make player moves on the board.
    def moveFromFile(self):
        pass

    # if the last player rock lands in his store, he gets extra turn
    def extraTurnCheck(self):
        pass

    # check for 2 stores total rocks, if = 48 then decide the winner.
    def checkWinning(self):
        pass

    # check which player turn is it and make the Ai player play instead.
    def timeOut(self):
        pass

    # save current game status.
    def saveGame(self):
        pass

    # load a saved game.
    def loadGame(self):
        pass


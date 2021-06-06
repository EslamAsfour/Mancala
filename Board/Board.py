class Board:

    def __init__(self):
        self.playing = False
        self.player = 1
        self.clicked_index = 0
        self.winning_player = 0
        # Player1 & 2 stores
        self.player1_store = 6
        self.player2_store = 13
        # zero-stone piles are the store of each player.
        self.piles = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

    # Start or end and choose player 1 or 2 to start
    def toggleGameStatus(self, player):
        self.player = player
        self.playing = not (self.playing)

        # if player 1 turn ends , it toggles to player 2.

    def togglePlayer(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

            # function to get last index if index = 6 or 13 to start new loop for both players

    def index_correction(self, index):
        if self.player == 1:
            if(index % 13 == 0):
                return 0
            else:
                return (index % 13)
        elif self.player == 2:
            if (index % 6 == 0 and index != 12 and index != 0):
                return 7
            else:
                return (index % 14)
        else:
            return


    # get clicked index
    # def get_clicked_index(self, clicked_index):
    #     self.clicked_index = clicked_index

    def get_input(self):
        print("Its Player ", self.player, " turn !")
        self.clicked_index = int(input("Please enter the starting index\n"))

    # make player moves on the board.
    def moveFromPile(self):
        print(self.piles[13],"    ",self.piles[12], self.piles[11], self.piles[10], self.piles[9], self.piles[8], self.piles[7],"   ",self.piles[6])
        print("      ",self.piles[0],self.piles[1],self.piles[2],self.piles[3],self.piles[4],self.piles[5],"               ")
        corrected_index = 0
        current_index = 0
        self.get_input()
        played_value = self.piles[self.clicked_index]
        self.piles[self.clicked_index] = 0
        for pile in range(1, played_value+1):
            if pile + self.clicked_index > 13:
                current_index = pile + self.clicked_index - (int((pile + self.clicked_index)/13)*13) - 1
            else:
                current_index = pile + self.clicked_index
            corrected_index = self.index_correction(current_index)
            self.piles[corrected_index] += 1
            if pile == played_value:
                self.checkWinning()
                self.extraTurnCheck(corrected_index)

    # if the last player rock lands in his store, he gets extra turn
    def extraTurnCheck(self, last_index):
        if last_index == self.player1_store and self.player == 1 and (self.piles[0] != 0 or self.piles[1] != 0 or self.piles[2] != 0 or self.piles[3] != 0 or self.piles[4] != 0 or self.piles[5] != 0):
            self.moveFromPile()
        elif last_index == self.player2_store and self.player == 2 and (self.piles[7] != 0 or self.piles[8] != 0 or self.piles[9] != 0 or self.piles[10] != 0 or self.piles[11] != 0 or self.piles[12] != 0):
            self.moveFromPile()
        else:
            self.togglePlayer()

            # check for 2 stores total rocks, if = 48 then decide the winner.

    def checkWinning(self):
        if self.piles[self.player1_store] + self.piles[self.player2_store] == 48:
            if self.piles[self.player1_store] > self.piles[self.player2_store]:
                self.winning_player = 1
            elif self.piles[self.player1_store] < self.piles[self.player2_store]:
                self.winning_player = 2
            else:
                self.winning_player = 3  # Tie
        else:
            self.winning_player = 0

            # check which player turn is it and make the Ai player play instead.

    def timeOut(self):
        pass

    # save current game status.
    def saveGame(self):
        pass

    # load a saved game.
    def loadGame(self):
        pass



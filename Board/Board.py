class Board:

    def __init__(self):
        self.playing = False
        self.player = 1
        self.wrong_turn = 0
        self.clicked_index = 0
        self.winning_player = 0
        # Player1 & 2 stores
        self.player1_store = 6
        self.player2_store = 13
        # zero-stone piles are the store of each player.
        self.piles = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

        # test cases
        #self.piles = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0]
        # self.piles = [4, 4, 4, 4, 4, 29, 0, 4, 32, 4, 4, 4, 4, 0]

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

    def prepMove(self):
        if (self.clicked_index != 6 and self.clicked_index != 5 and self.clicked_index != 4 and self.clicked_index != 3 and self.clicked_index != 2 and self.clicked_index != 1 and self.clicked_index != 0) and self.player == 1:
            self.wrong_turn = 1

            return
        elif (self.clicked_index != 13 and self.clicked_index != 12 and self.clicked_index != 11 and self.clicked_index != 10 and self.clicked_index != 9 and self.clicked_index != 8 and self.clicked_index != 7) and self.player == 2:
            self.wrong_turn = 2

            return
        else:
            self.wrong_turn = 0
            depth = self.piles[self.clicked_index]
            self.piles[self.clicked_index] = 0
            self.playMove(depth)
            self.checkToEnd()
            return

    def playMove(self, depth):

        self.clicked_index += 1

        # Stop Condition
        if depth == 0:
            return


        if self.clicked_index > 13:
            self.clicked_index = 0

        # Check for the plus one Turn or End game
        if depth == 1:
            if self.player == 1 and self.clicked_index == 6:
                self.piles[self.clicked_index] += 1
                self.checkToEnd()
                self.extraTurn()
                return
            elif self.player == 2 and self.clicked_index == 13:
                self.piles[self.clicked_index] += 1
                self.checkToEnd()
                self.extraTurn()
                return
            else:
                self.togglePlayer()

        if self.clicked_index == self.player2_store and self.player == 1:
            self.clicked_index = 0
        elif self.clicked_index == self.player1_store and self.player == 2:
            self.clicked_index = 7

        self.piles[self.clicked_index] += 1
        return self.playMove(depth - 1)

    def printPiles(self):
        print(self.piles[13], "    ", self.piles[12], self.piles[11], self.piles[10], self.piles[9], self.piles[8],
              self.piles[7], "   ", self.piles[6])
        print("      ", self.piles[0], self.piles[1], self.piles[2], self.piles[3], self.piles[4], self.piles[5],
              "               ")

    def checkToEnd(self):
        if self.piles[self.player1_store] + self.piles[self.player2_store] == 48:
            if self.piles[self.player1_store] > self.piles[self.player2_store]:
                self.winning_player = 1
            elif self.piles[self.player1_store] < self.piles[self.player2_store]:
                self.winning_player = 2
            else:
                self.winning_player = 3  # Draw
        else:
            self.winning_player = 0


    def extraTurn(self):
        if self.winning_player == 0:
            if self.player == 1 and (
                    self.piles[0] != 0 or self.piles[1] != 0 or self.piles[2] != 0 or self.piles[3] != 0 or self.piles[
                4] != 0 or self.piles[5] != 0):
                print("Its Player ", self.player, " turn again, you've got an extra turn!")
                return
            elif self.player == 2 and (
                    self.piles[7] != 0 or self.piles[8] != 0 or self.piles[9] != 0 or self.piles[10] != 0 or self.piles[
                11] != 0 or self.piles[12] != 0):
                print("Its Player ", self.player, " turn again, you've got an extra turn!")
                return
            else:
                self.togglePlayer()
                return

    # check which player turn is it and make the Ai player play instead.

    def timeOut(self):
        pass

    # save current game status.
    def saveGame(self):
        # with open('gamefile.txt', 'w') as filehandle:
        #     filehandle.writelines("%s\n" % pile for pile in self.piles)
        pass

    # load a saved game.
    def loadGame(self):
        pass

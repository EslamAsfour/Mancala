import Board
import sys
import copy
class player:
    def __init__(self,depth,isplayer1):
        self.depth=depth
        self.ispalyer1=isplayer1

    def Get_children(self,board,isplayer1):
        children=[]
        count=0
        if isplayer1:
            for i in range(6):
                copy_board = board[:]
                j = copy_board[i]
                copy_board[i]=0
                if j!=0:
                    for k in range(j):
                        index=k+i+1
                        while index > 13:
                            index = index - 14
                        copy_board[index]+=1
                        count=index
                if count==6:
                    children.append((copy_board, i,True))
                else:
                    children.append((copy_board, i,False))

        else:
            for i in range(7,13):
                copy_board = board[:]
                j = copy_board[i]
                copy_board[i]=0
                if j!=0:
                    for k in range(j):
                        index = k + i + 1
                        while index > 13:
                            index = index - 14
                        copy_board[index] += 1
                        count = index

                if count==13:
                    children.append((copy_board, i,True))
                else:
                    children.append((copy_board, i,False))


        return children


    def Heuristic(self,board,isplayer1):
        player1stones=0
        #for i in range(6):
           # player1stones+=board[i]
        player1stones+=board[6]*3
        player2stones=0
        #for j in range(7,13):
            #player2stones+=board[j]
        player2stones+=board[13]*3
        if isplayer1:
            return player1stones-player2stones
        else:
            return player2stones-player1stones



    def minimax(self,board):

        def game_is_over(board):
            if (board[6]+board[13])==48:
                return True
            else:
                return False


            """game_over=True
            for i in range(6):
                if board[i]!=0:
                    game_over=False
                    break
            if not game_over:

                for j in range(7,13):
                    if board[j]!=0:
                        game_over=False
                        break
            return game_over"""

        def adjust(board,index,isplayer1):
            if index==-1:
                if isplayer1:
                    for i in range(6):
                        if board[i]!=0:
                            return i
                else:
                    for i in range(7,13):
                        if board[i]!=0:
                            return i
            else:
                return index


        def MinimaxHelper(current_board,depth,isplayer1,isMax):
            if game_is_over(current_board):
                if self.ispalyer1:
                    return current_board[6]-current_board[13]
                else:
                    return current_board[13]-current_board[6]
            elif depth==0:
                return self.Heuristic(current_board,self.ispalyer1),-1
            children=self.Get_children(current_board,isplayer1)
            if isMax:
                best_score=-1000
                should_replace=lambda x: x>best_score
            else:
                best_score=1000
                should_replace=lambda x: x<best_score

            best_move=-1

            for child in children:
                child_board,child_move,Play_again=child
                if isMax:
                    temp_val=-1000
                else:
                    temp_val=1000

                if current_board[child_move]!=0:
                    if Play_again==True:
                        temp_val= MinimaxHelper(child_board, depth-1 , isplayer1,isMax)[0]
                    else:
                        temp_val = MinimaxHelper(child_board, depth - 1, not isplayer1, not isMax)[0]

                if should_replace(temp_val):
                    best_score = temp_val
                    best_move = child_move
            return (best_score,best_move)
        score,move= MinimaxHelper(board,self.depth,self.ispalyer1,True)

        move=adjust(board,move,self.ispalyer1)

        return move




def minimax(board,depth,alpha,beta,isplayer1):
    p2 = player(depth, isplayer1)
    return p2.minimax(board)

sys.setrecursionlimit(30000)
p3=player(5,False)
board= Board
board.piles=[0,0,3,4,2,3,14,0,0,0,0,4,0,18]
index= p3.minimax(board.piles)
print(index)

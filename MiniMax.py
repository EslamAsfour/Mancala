import Board
import sys
import copy
class player:
    def __init__(self,depth,isplayer1):
        self.depth=depth
        self.ispalyer1=isplayer1

    def Get_children(self,board,isplayer1,isStealing):
        pilesDict = {0: 12, 1: 11, 2: 10, 3: 9, 4: 8, 5: 7, 12: 0, 11: 1, 10: 2, 9: 3, 8: 4, 7: 5}
        children=[]
        count=0
        if isStealing==False:
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
        else:
            if isplayer1:
                for i in range(6):
                    copy_board = board[:]
                    j = copy_board[i]
                    copy_board[i] = 0
                    if j != 0:
                        for k in range(j):
                            index = k + i + 1
                            while index > 13:
                                index = index - 14
                            copy_board[index] += 1
                            count = index
                    if count == 6:
                        children.append((copy_board, i, True))
                    elif count<6 and copy_board[count]==1 and copy_board[pilesDict.get(count)]!=0:
                        copy_board[count]=0
                        copy_board[6]+=copy_board[pilesDict.get(count)]+1
                        copy_board[pilesDict.get(count)]=0
                        children.append((copy_board, i, False))
                    else:
                        children.append((copy_board, i, False))

            else:
                for i in range(7, 13):
                    copy_board = board[:]
                    j = copy_board[i]
                    copy_board[i] = 0
                    if j != 0:
                        for k in range(j):
                            index = k + i + 1
                            while index > 13:
                                index = index - 14
                            copy_board[index] += 1
                            count = index

                    if count == 13:
                        children.append((copy_board, i, True))
                    elif count > 6 and count < 13 and copy_board[count] == 1 and copy_board[pilesDict.get(count)] != 0:
                        copy_board[count] = 0
                        copy_board[13] += copy_board[pilesDict.get(count)] + 1
                        copy_board[pilesDict.get(count)] = 0
                        children.append((copy_board, i, False))
                    else:
                        children.append((copy_board, i, False))


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



    def minimax(self,board,alpha,beta,isStealing):

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


        def MinimaxHelper(current_board,depth,alpha,beta,isplayer1,isMax,isStealing):
            if game_is_over(current_board):
                if self.ispalyer1:
                    return current_board[6]-current_board[13],-1
                else:
                    return current_board[13]-current_board[6],-1
            elif depth==0:
                return self.Heuristic(current_board,self.ispalyer1),-1
            children=self.Get_children(current_board,isplayer1,isStealing)
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

                        temp_val = MinimaxHelper(child_board, depth-1 ,alpha,beta, isplayer1,isMax,isStealing)[0]
                    else:
                        temp_val = MinimaxHelper(child_board, depth - 1,alpha,beta, not isplayer1, not isMax,isStealing)[0]
                else:
                    pass

                if should_replace(temp_val):
                    best_score = temp_val
                    best_move = child_move
                if isMax:
                    alpha=max(alpha,temp_val)
                else:
                    beta=min(beta,temp_val)
                if alpha>beta:
                    break
            return (best_score,best_move)
        score,move= MinimaxHelper(board,self.depth,alpha,beta,self.ispalyer1,True,isStealing)

        move=adjust(board,move,self.ispalyer1)

        return move




def minimax(board,depth,alpha,beta,isplayer1,isStealing):
    p2 = player(depth, isplayer1)
    return p2.minimax(board,alpha,beta,isStealing)

sys.setrecursionlimit(30000)
p3=player(5,False)
board= Board
board.piles=[0,0,0,0,0,0,12,0,0,0,0,0,1,35]
index= p3.minimax(board.piles,-1000,1000,True)
print(index)

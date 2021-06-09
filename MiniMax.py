import Board
import sys
import copy

def Update_index(board,play_index):
    copy_board=board[:]
    count = 0
    if play_index!=6 and play_index!=13:
        while play_index>13:
            play_index=play_index-14

        j=copy_board[play_index]
        copy_board[play_index] = 0

        if j!=0:
            for i in range (j):
                index=play_index+i+1
                while index > 13 :
                    index = index-14
                count=index
                copy_board[index]=copy_board[index]+1
        #print(board.piles)
    if (count==6 and play_index>=0 and play_index<6) or (count==13 and play_index>6 and play_index<13):
        play_again_flag=True
    else:
        play_again_flag=False
    return copy_board,play_again_flag



zeros=[0,0,0,0,0,0]

def minimax(board,depth, alpha, beta, maximizingPlayer):
    boards=[]
    for i in range (depth+1):
        boards.append(copy.deepcopy(board))

    if depth==0 or (board[6]+board[13])>20 :
        #if maximizingPlayer ==1:
        if board[6]>board[13]:
            return board[6],None
        else:
            return -(board[13]),None
        #elif maximizingPlayer ==2:
            #if board.piles[13]>board.piles[6]:
                #return board.piles[13],None
            #else:
                #return -1000,None
    if maximizingPlayer == True:
        best_index = 0
        maxEval = -1000
        for index in range(7,13):
            if board[index] != 0:
                boards[depth - 1],play_again_flag = Update_index(boards[depth], index)
                #print(index)
                #print((board.piles))
                if play_again_flag==True:
                    eval, best_index = minimax(boards[depth - 1], depth - 1, alpha, beta, True)
                else:
                    eval, best_index = minimax(boards[depth - 1], depth - 1, alpha, beta, False)

                if eval >= maxEval:
                    best_index = index
                maxEval = max(maxEval, eval)
                #alpha = max(alpha, eval)
                #if beta <= alpha:
                    #break
        if board[7]==0 and board[8]==0 and board[9]==0 and board[10]==0 and board[11]==0 and board[12]==0:
            eval, best_index = minimax(boards[depth-1],depth-1, alpha, beta, False)
        
        return maxEval, best_index

    else:
        bestmin_index = 0
        minEval = +1000
        for index in range(6):
            if board[index] != 0:
                boards[depth-1],play_again_flag = Update_index(boards[depth], index)

                #print(index)
                #print((board.piles))
                if play_again_flag==True:
                    eval, bestmin_index = minimax(boards[depth - 1], depth - 1, alpha, beta, False)

                else:
                    eval, bestmin_index = minimax(boards[depth - 1], depth - 1, alpha, beta, True)
                minEval = min(minEval, eval)
                #beta = min(beta, eval)
                #if beta <= alpha:
                    #break
        if board[0]==0 and board[1]==0 and board[2]==0 and board[3]==0 and board[4]==0 and board[5]==0:
            eval, best_index = minimax(boards[depth-1],depth-1, alpha, beta, True)
            pass
        return minEval, bestmin_index


sys.setrecursionlimit(30000)
board= Board
board.piles=[4, 4, 4, 4, 4, 4, 0, 4, 0, 5, 5, 5, 5, 0]
eval,index= minimax(board.piles,7,-1000,1000,True)
print(index)
print(eval)
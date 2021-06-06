



def PrintList(ls):
    print()
    print()
    print("-----------------------------------------------")
    print("R2 : Sum|{}||{}||{}||{}||{}||{}||{}| ".format(ls[13],ls[12],ls[11],ls[10],ls[9],ls[8],ls[7]))
    
    print("R1 :       |{}||{}||{}||{}||{}||{}| Sum |{}|".format(ls[0],ls[1],ls[2],ls[3],ls[4],ls[5],ls[6]))
    print("-----------------------------------------------")
    print()
    
    
def PlayMove(ls ,Index, depth ,Player):
    #Stop Condition
    if depth == 0:
        return ls,False
    
    if Index > 13:
        Index = 0
        
    # Check for the plus one Turn
    if depth == 1 and Player == 1 and Index == 6:
        ls[Index] += 1
        print("Player 1  : +1")
        return ls ,True
    if depth == 1 and Player == 2 and Index == 13:
        print("Player 2  : +1")
        ls[Index] += 1
        return ls ,True
        
    
    if Index == 13 and Player == 1:
        Index = 0
    elif Index == 6 and Player == 2:
        Index = 7
        
    ls[Index] += 1
    return PlayMove(ls,Index+1 , depth-1, Player)
    
    
def PrepMove(ls, index, player , flag):
    depth = ls[index]
    ls[index] = 0 
    ls, flag = PlayMove(ls,index+1,depth,player)
    return ls, flag
           
 


ls = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
index = 0
player =1
PrintList(ls)
flag = False
while 1:
    print("     Player {} Turn".format(player))
    index = int(input('     Enter Index :'))
    ls,flag = PrepMove(ls,index,player,flag)
    
    if player ==1 and flag ==False:
        player =2
    elif player == 2 and flag == False:
        player = 1
    PrintList(ls)




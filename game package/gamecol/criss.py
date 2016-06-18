##RKB developer..... everything is easy you only need the perfect algorithm and the imagination
from random import randint
import os
board=list(' '*9)
def reset():
    global board
    board=list(' '*9)

def computer(hm,pc):
    print "computer plays (press any key to continue)"
    raw_input()
    ##for placing the mark depending on win nd loose 
    for i in xrange(0,9):##check whether computer is gonna win    
        if board[i]==' ':   
           board[i]=pc
           if checkwin()==1:
              board[i]=' '
              return i+1
           board[i]=' '
  
    for i in xrange(0,9):##check whether player is gonna win
        if board[i]==' ':
           board[i]=hm
           if checkwin()==1:              
              board[i]=' '
              return i+1
           board[i]=' '  

                                 
    ##for corner and side check check 
    if hm=='X':
       if i==8:  ## this comparisons is to check weahther there was no place to either stop an atack or issue an wiining move
          if board[4]==' ':
             i=4
	  elif board[1]==' ':
               i=1
	  elif board[3]==' ':
               i=3
	  elif board[5]==' ':
	       i=5
	  elif board[7]==' ':
	       i=7         
          elif board[0]==' ':
	       i=0         
	  elif board[2]==' ':
	       i=2
	  elif board[6]==' ':
	       i=6      
	 
    if hm=='O':
        if i==8:
          if board[0]==' ':
	       i=0         
          elif board[8]==' ':
               i=8
          elif board[1]==' ' and board[2]==' ':
	       i=2
	  elif board[4]==' ' and board[6]==' ':
	       i=6
          elif board[7]==' ' and board[8]==' ':
	       i=8
          
    return i+1
    
    
     



def checkwin():
    if(board[1-1]==board[2-1] and board[2-1]==board[3-1] and not board[1-1]==' '):
       return 1
    elif(board[4-1]==board[5-1] and board[5-1]==board[6-1] and not board[4-1]==' '):
         return 1
    elif(board[7-1]==board[8-1] and board[8-1]==board[9-1] and not board[7-1]==' '):
         return 1
    elif(board[1-1]==board[4-1] and board[4-1]==board[7-1] and not board[1-1]==' '):
         return 1
    elif(board[2-1]==board[5-1] and board[5-1]==board[8-1] and not board[2-1]==' '):
         return 1
    elif(board[3-1]==board[6-1] and board[6-1]==board[9-1] and not board[3-1]==' '):
         return 1 
    elif(board[1-1]==board[5-1] and board[5-1]==board[9-1] and not board[1-1]==' '):
         return 1 
    elif(board[3-1]==board[5-1] and board[5-1]==board[7-1] and not board[3-1]==' '):
       return 1
    elif not ' ' in board:
         return -1
    else:
         return 0 
         

def boarddesign(i,hm,pc):
    print board[1-1]+"  | "+board[2-1]+" | "+board[3-1]
    print "---|---|---"
    print board[4-1]+"  | "+board[5-1]+" | "+board[6-1]
    print "---|---|---"
    print board[7-1]+"  | "+board[8-1]+" | "+board[9-1]
    player=' '
    if i%2==0:
       while True:
             s=int(raw_input("\nEnter the plce for player by :"))
             if not board[s-1]==' ':
                print "\nwrong option its filled try again!!!"
             else:
                 break
       board[s-1]=hm 
       player='h'
    else:
        s=int(computer(hm,pc))
        board[s-1]=pc
        player='c'
    return player
    
                       

def game(i,hm,pc):
      raw_input("\nThis a tick tac toe game that is to illustrate the very basics of A.I in algorithm\n\n")
      while checkwin()==0:
             os.system('cls')
             player=boarddesign(i,hm,pc) ## the game is played here this while loop holds it. the later is just results
             i=i^1   
      
      os.system('cls')
      print board[1-1]+"  | "+board[2-1]+" | "+board[3-1]
      print "---|---|---"
      print board[4-1]+"  | "+board[5-1]+" | "+board[6-1]
      print "---|---|---"
      print board[7-1]+"  | "+board[8-1]+" | "+board[9-1]
      
      if checkwin()==1:
         if(player=='h'):
            print "PLAYER WIN:: hence proved human is intelligent"
         else:
             print "Computer wins. it is more intelligent than you"   
      if checkwin()==-1:
         print "Its a draw :: your intelligence is equal to a computer."
      reset()

def player():	   
    n='y'
    while n=='y':
	    os.system("cls")
            print str(1)+"  | "+str(2)+" | "+str(3)
            print "---|---|---"
            print str(4)+"  | "+str(5)+" | "+str(6)
            print "---|---|---"
            print str(7)+"  | "+str(8)+" | "+str(9)
            print "\n The board lay out\n"
	    a=raw_input("Welcome to the game!!!!\n\ndo you want to play first:")
	    i=0
	    if a=='y':
	       i=0
	       hm='X'
	       pc='O'
	    else:
		i=1
		hm='O'
		pc='X'
	    game(i,hm,pc)
	    n=raw_input("\n\nDo you wnna challenge the computer again:")                    




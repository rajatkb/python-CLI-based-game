##RKB..Dev.. everything is simple with the best algorithm and imagination :-) enjoy gaming.
##if you defeat the game do improve its algorithm and if possible share to me and also other :-)

import os
from random import shuffle
import platform

if platform.system()=='Linux':
    cs='clear'
else:
     cs='cls'


def turnboard(board):
    temp=makeboard(" "," ")
    for i in range(8):
        for j in range(8):
            temp[7-i][7-j]=board[i][j]
    return temp
             
def makeboard(hm,pc): #makes the board
    board=[]
    for x in range(8):
        board.append(list(" "*8))
    board[3][3]=hm
    board[3][4]=pc
    board[4][3]=pc
    board[4][4]=hm
    return board

def displayboard(board): # display the current sttus of the board
    print "   1  2  3  4  5  6  7  8",
    for x in range(8):
        print "\n  "+"|--"*8+"|"
        print str(x+1),
        for y in range(8):
            print "|"+board[x][y],
        print "|",
    print "\n  "+"|--"*8+"|"

def userinput(board,mk): #gets the input from user
    while True:
	    cood=[]
            cood.append(int(raw_input("Enter the row(horiziontal):"))-1)
	    cood.append(int(raw_input("Enter the column(vertical):"))-1)
	    if not board[cood[0]][cood[1]]==" ":
               raw_input("Try again the space is not available or you have given wrong entry")
               del cood
            else:
                board[cood[0]][cood[1]]=mk
                return cood
    
def reversemark(board,hm,pc,x,y): #reverses the marks here rows are x and y are column. conratry to general coordinate system	       
    l=0 
    while l<2:
           #side by side remarking
		  f='n'
		  temp=[]
		  for j in xrange(y+1,8): 
		      if board[x][j]==" ":
		         break
		      elif board[x][j]==hm:
		             f='y'
		             break
		      elif board[x][j]==pc:
		               temp.append([x,j])
		           
		  if bool(temp) and f=='y':
		     for [i,j] in temp:
		         board[i][j]=hm                 
		  del temp
	    #top down remarking
		  f='n'
		  temp=[]
		  for i in xrange(x+1,8): 
		      if board[i][y]==" ":
		         break
		      elif board[i][y]==hm:
		             f='y'
		             break
		      elif board[i][y]==pc:
		               temp.append([i,y])
		           
		  if bool(temp) and f=='y':
		     for [i,j] in temp:
		         board[i][j]=hm                 
		  del temp
	    #diagonal remarking
		  f='n'
		  i=x+1
		  j=y+1
		  temp=[]
		  while i<8 and j<8: 
			      if board[i][j]==" ":
				 break
			      elif board[i][j]==hm:
				     f='y'
				     break
			      elif board[i][j]==pc:
				       temp.append([i,j])
			      i+=1
			      j+=1     
		  if bool(temp) and f=='y':
		     for [i,j] in temp:
		         board[i][j]=hm                 
		  del temp
	    #diagonal remarking reverse
		  f='n'
		  i=x+1
		  j=y-1
		  temp=[]
		  while i<8 and j>=0: 
			      if board[i][j]==" ":
				 break
			      elif board[i][j]==hm:
				     f='y'
				     break
			      elif board[i][j]==pc:
				       temp.append([i,j])
			      i+=1
			      j-=1     
		  if bool(temp) and f=='y':
		     for [i,j] in temp:
		         board[i][j]=hm                 
		  del temp
                  x=7-x
                  y=7-y
                  l+=1
                  board=turnboard(board)    
    return board
 
def checkwin(board,mkp,mks): ##markprimary=mkp and marksecondary=mks
    countmkp=countmks=0
    for i in range(8):
        for j in range(8):
            if board[i][j]==mkp:
               countmkp=countmkp+1
            elif board[i][j]==mks:
                 countmks=countmks+1
    if countmkp>countmks:
       return mkp
    else:
        return mks
def getscore(board,mk):
    score=0
    for i in range(8):
        for j in range(8):
            if board[i][j]==mk:
               score+=1
    return score


def copyboard(board):
    temp=makeboard(" "," ")
    for i in range(8):
        for j in range(8):
            temp[i][j]=board[i][j]
    return temp


def aiinput(board,pc,hm):
    boardt=copyboard(board)
    scorecrd=[]
    for i in range(8):
        for j in range(8):
            if boardt[i][j]==" ":
               q=0
               mk=mk2=' '
               while q<2:               
		       if q==0:
                          mk=pc
                       else:
                           mk2=hm
                       boardt[i][j]=mk
		       boardt=reversemark(boardt,mk,mk2,i,j)
		       scorecrd.append([getscore(boardt,mk),i,j])
		       boardt=copyboard(board)
                       q+=1
               
    mark=[0,0,0]
    shuffle(scorecrd)    
    for [s,i,j] in scorecrd:
         if s>mark[0]:
            mark=[s,i,j]       
    i=mark[1]
    j=mark[2]
    board[i][j]=pc
    return [i,j]

 
def playwithcomp():
        os.system(cs)
        print "WELCOME TO THE REVERSI GAME \n\n BE WARNED THE GAME WILL DEFEAT YOU !!!!!"
        hm=pc=' ' 
        itr=0
	choice=raw_input("\nDo you wanna play first(y/n):")
        if choice=='y':
           itr=1
           hm="X"
           pc="O"
        else:
            itr=0
            hm="O"
            pc="X"	
	board=makeboard(hm,pc)
        raw_input("\nPRESS ENTER TO CONTINUE")
	while True:
		itr=itr+1
		os.system(cs)
		displayboard(board)
		if itr%2==0:
                        print "You are ",hm," and computer is ",pc
			print "\nYour score is ",getscore(board,hm),"and computer score is ",getscore(board,pc)
			r,c=userinput(board,hm)
			board=reversemark(board,hm,pc,r,c)       
		else:
			raw_input("computer plays\n")
			r,c=aiinput(board,pc,hm)
		        board=reversemark(board,pc,hm,r,c)
		f='y'
		for i in range(8):
		    for j in range(8):
		        if board[i][j]==" ":
		           f='n'
		           break
		if f=='y':
		   break    
	mk=checkwin(board,hm,pc)
	if mk==hm:
	   print "You win hence proved man is still intelligent"
	else:
	    print "Cant believe you losed against a dumb machine"
      	
        
       
    

     


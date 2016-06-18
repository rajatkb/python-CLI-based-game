from random import randint   #this is for the random number genrator
import os  #this is for clearing the screen

class module:
	def menu(self):    #the default menu
	    print " HELLO WELCOME TO THE hangman "
	    a=raw_input("\n\n\tDo you wanna continue:")
	    if a=='y':
	       os.system('cls')
	       a=module()
	       a.game()
               raw_input()
            else: 
		print "bye"

	def game(self):   #the game works as for managing the list of the number
	    mlist=["Antarctica","India","Canada","Pakistan","Afghanistan","Columbia","Russia","Nederlands","Africa"]
	    word=mlist[randint(0,len(mlist)-1)]
	    a=module()
            a.algorithm(word)  

	def algorithm(self,word): #tis is the real stuff
	       #currently testing
	    h="hangman"  #the word to be killed
	    dead=word     #instance to be changed as the word is found out
	    l=0
	    win=0
	    default="_"*(len(dead))
	    print "\n\n"
	    raw_input("Press any key to continue")
	    
	    while not h==("?"*len(h)):  
		   os.system('cls')
		   print "\t\nNow you have a country name make the gusses right!! game on\n\n"
		   i=0
		   while i<=(len(default)-1):
			 print default[i],
			 i=i+1
	    
		   i=0
		   print "      ",    
		   while i<=(len(h)-1):
			  print h[i],
			  i=i+1

                  
		   answer=raw_input("\n\nENTER YOUR GUESS:")
		   answer=list(answer)
		   for answer in answer:
		       if  dead.find(answer)!=-1:
			   s=list(default)
			   s[dead.find(answer)]=dead[dead.find(answer)]
			   default="".join(s)
			   s=list(dead)
			   s[dead.find(answer)]="_"
			   dead="".join(s)
		       else:
			    s=list(h)
			    s[l]="?"
			    h="".join(s)
			    l=l+1
		   if default==word:
		       win=1
		       break
	    
	    print "\nFinally!!!!!!\n"     
	    i=0
	    while i<=(len(default)-1):
		  print default[i],
		  i=i+1
	    i=0
	    print "      ",    
	    while i<=(len(h)-1):
		  print h[i],
		  i=i+1        
	    a=module()
            a.winmessege(win)     
	    
	def winmessege(self,win):
	    if win==1:
	       print "\n\nYou win !!!! yippe"
	    if win==0:
	       print "\n\n You loose !!! toing o.O"
    

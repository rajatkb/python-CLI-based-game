import gamecol
import os
while True:
 os.system('cls')
 print "WELCOME to the game collection"
 print "\nMAKE YOUR CHOICE"
 print "\na.HANGMAN       b.TIC TAC TOE    c.REVERSI	d.Exit"
 a=raw_input("\nINPUT your choice:")
 if a=='a':
    os.system('cls')
    b=gamecol.module()
    b.menu()
 elif a=='b':
      os.system('cls')
      gamecol.player()
 elif a=='c':
      os.system('cls')
      gamecol.playwithcomp()
 elif a=='d':
      exit()
 else:
     print "\n\nwrong option (press enter to continue)"
     raw_input()



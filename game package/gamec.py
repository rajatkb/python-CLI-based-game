import gamecol
import os
import platform
while True:
 if platform.system()=='Linux':
    cs='clear'
 else:
     cs='cls'
 os.system(cs)
 print "WELCOME to the game collection"
 print "\nMAKE YOUR CHOICE"
 print "\na.HANGMAN       b.TIC TAC TOE    c.REVERSI	d.Exit"
 a=raw_input("\nINPUT your choice:")
 if a=='a':
    os.system(cs)
    b=gamecol.module()
    b.menu()
 elif a=='b':
      os.system(cs)
      gamecol.player()
 elif a=='c':
      os.system(cs)
      gamecol.playwithcomp()
 elif a=='d':
      exit()
 else:
     print "\n\nwrong option (press enter to continue)"
     raw_input()



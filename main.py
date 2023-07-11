#imports all the function to be executed
from instructions import instruct
from placeboat import place_boat
from aiboatgenerator import aiboat
from checkboat import checkcoords
from aicheckboat import aiboatguess
import time
from checkwin import wincheck
from quit import quit
from save import save_game

#Options for the User. The progam follows according to user input
def options():
  from board1 import board
  from display import displayboard
  global save
  from save import save
  #asks the user for input for what function they want 
  option = int(input(" Welcome to battleboats!"
                    "\n ========================"
                    "\n  "
                    "\n Which option would you like to choose-"
                    "\n 1. Instructions"
                    "\n 2. New game"
                    "\n 3. Quit"
                    "\n 4. Resume game"
                    "\n "))
  
  #executes instructions
  if option == 1:
    print(instruct())
    print(displayboard(board))
    print(options())

  #executes new game
  if option == 2:
    print("New game:  "
         "\n ")
    #repeats the input 5 times 
    for x in range(1,6):
      print(place_boat(board))
      print(displayboard(board))
      #generates ai boats
    for y in range (1, 6):
      print(aiboat())
    for z in range(1, 64):
      print(checkcoords())
      time.sleep(3)
      print(aiboatguess())
      print(wincheck())
      
  #executes quitting the game
  if option == 3:
    print(quit())

  if option == 4:
    save = True
print(options())
    

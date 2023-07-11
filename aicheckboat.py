#Checks if ai has guessed a human player boat or not. Outputs if it has
def aiboatguess():
  from random import randint
  from board1 import board
  from display import displayboard
  x = randint(0, 8)
  y = randint(0, 8)
  #checks for a hit
  if board[x][y] == "b":
    board[x][y] = "H"
    print("The enemy hit one of your battleships!")
    print(displayboard(board))
    return " "
  #checks for a miss
  if board[x][y] == " ":
     board[x][y] = "M"
     print("The enemy missed!")
     print(displayboard(board))
     return " "
  #makes sure the computer doesnt guess the spot twice
    
#Generates boats for the ai on a separate board
def aiboat():
  from board2 import board_2
  from random import randint
  for i in range(0,5):
    x = randint(1,8)
    y = randint(1,8)
    if board_2[x][y] == " ":
      board_2[x][y] = "b"
      return " "
      #prevents computer from putting boats on top of each other
    elif board_2[x][y] == "M" or "H" or "b":
      print(aiboat())
  print(" The enemy has added his boats")
  return " "
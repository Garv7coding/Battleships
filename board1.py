#Board for the human player
from save import save
board = [[" 0", "1", "2", "3", "4", "5", "6", "7", "8"],
         [" 1", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 2", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 3", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 4", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 5", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 6", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 7", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 8", " ", " ", " ", " ", " ", " ", " ", " "]]

def board1saved():
  from board1 import board
  if save == True:
    file = open("board1saved.csv", "r")
    file.read("board1saved.csv")
    board = file
    file.close()
#my attempt at resuming the game. It didn't work as planned
def resume():
  from save import save
  from board1 import board
  from board2 import board_2
  if save == True:
    file1 = open("board1saved.csv", "r")
    file1.read
    board1 = file1
    file1.close()
    file2 = open("board2saved.csv", "r")
    file2.read
    board_2 = file2
    file2.close()
    print(board1)
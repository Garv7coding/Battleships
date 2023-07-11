#checks if computer or user has won 
def wincheck():
  from board1 import board
  from board2 import board_2
  from quit import quit
  #matches for board  
  for a in range(0, 8):
    for b in range(0, 8):
      if board[a][b] == "b":
        return " "
  else:
    return "Computer wins!"
    print(quit())
  for a in range(0, 8):
    for b in range(0, 8):
      if board_2[a][b] == "b":
        return " "
  else:
    return "Player wins!"
    print(quit())
    
  
    
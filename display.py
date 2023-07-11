#board to be displayed 
disboard = [[" 0", "1", "2", "3", "4", "5", "6", "7", "8"],
         [" 1", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 2", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 3", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 4", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 5", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 6", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 7", " ", " ", " ", " ", " ", " ", " ", " "],
         [" 8", " ", " ", " ", " ", " ", " ", " ", " "]]

def displayboard(board):
  print( board[0][0], "  │", board[0][1], " │", board[0][2], " │", board[0][3], " │", board[0][4], " │", board[0][5], " │", board[0][6], " │", board[0][7], " │", board[0][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( board[1][0], "  │", board[1][1], " │", board[1][2], " │", board[1][3], " │", board[1][4], " │", board[1][5], " │", board[1][6], " │", board[1][7], " │", board[1][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( board[2][0], "  │", board[2][1], " │", board[2][2], " │", board[2][3], " │", board[2][4], " │", board[2][5], " │", board[2][6], " │", board[2][7], " │", board[2][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( board[3][0], "  │", board[3][1], " │", board[3][2], " │", board[3][3], " │", board[3][4], " │", board[3][5], " │", board[3][6], " │", board[3][7], " │", board[3][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( board[4][0], "  │", board[4][1], " │", board[4][2], " │", board[4][3], " │", board[4][4], " │", board[4][5], " │", board[4][6], " │", board[4][7], " │", board[4][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( board[5][0], "  │", board[5][1], " │", board[5][2], " │", board[5][3], " │", board[5][4], " │", board[5][5], " │", board[5][6], " │", board[5][7], " │", board[5][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( board[6][0], "  │", board[6][1], " │", board[6][2], " │", board[6][3], " │", board[6][4], " │", board[6][5], " │", board[6][6], " │", board[6][7], " │", board[6][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( board[7][0], "  │", board[7][1], " │", board[7][2], " │", board[7][3], " │", board[7][4], " │", board[7][5], " │", board[7][6], " │", board[7][7], " │", board[7][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( board[8][0], "  │", board[8][1], " │", board[8][2], " │", board[8][3], " │", board[8][4], " │", board[8][5],  " │", board[8][6], " │", board[8][7], " │", board[8][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  return " "

#board displayed for ai's boat guesses
def displayboard2(disboard):
  print( disboard[0][0], "  │", disboard[0][1], " │", disboard[0][2], " │", disboard[0][3], " │", disboard[0][4], " │", disboard[0][5], " │", disboard[0][6], " │", disboard[0][7], " │", disboard[0][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( disboard[1][0], "  │", disboard[1][1], " │", disboard[1][2], " │", disboard[1][3], " │", disboard[1][4], " │", disboard[1][5], " │", disboard[1][6], " │", disboard[1][7], " │", disboard[1][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( disboard[2][0], "  │", disboard[2][1], " │", disboard[2][2], " │", disboard[2][3], " │", disboard[2][4], " │", disboard[2][5], " │", disboard[2][6], " │", disboard[2][7], " │", disboard[2][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( disboard[3][0], "  │", disboard[3][1], " │", disboard[3][2], " │", disboard[3][3], " │", disboard[3][4], " │", disboard[3][5], " │", disboard[3][6], " │", disboard[3][7], " │", disboard[3][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( disboard[4][0], "  │", disboard[4][1], " │", disboard[4][2], " │", disboard[4][3], " │", disboard[4][4], " │", disboard[4][5], " │", disboard[4][6], " │", disboard[4][7], " │", disboard[4][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( disboard[5][0], "  │", disboard[5][1], " │", disboard[5][2], " │", disboard[5][3], " │", disboard[5][4], " │", disboard[5][5], " │", disboard[5][6], " │", disboard[5][7], " │", disboard[5][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( disboard[6][0], "  │", disboard[6][1], " │", disboard[6][2], " │", disboard[6][3], " │", disboard[6][4], " │", disboard[6][5], " │", disboard[6][6], " │", disboard[6][7], " │", disboard[6][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( disboard[7][0], "  │", disboard[7][1], " │", disboard[7][2], " │", disboard[7][3], " │", disboard[7][4], " │", disboard[7][5], " │", disboard[7][6], " │", disboard[7][7], " │", disboard[7][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  print( disboard[8][0], "  │", disboard[8][1], " │", disboard[8][2], " │", disboard[8][3], " │", disboard[8][4], " │", disboard[8][5], " │", disboard[8][6], " │", disboard[8][7], " │", disboard[8][8], " │")
  print(" ────┼────┼────┼────┼────┼────┼────┼────┼────┼")
  return " "
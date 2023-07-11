#places boats on the board
def place_boat(board):
  from board1 import board
  #from alphtonum import x_coords_converter
  #asks player for input
  x = int(input("Enter Y coordinate:   "))
  y = int(input("Enter X coordinate:   "))
  #print(x_coords_converter())
  #validates if input is correct
  if x > 8 or x < 0:
    print("Enter co-ordinates between 1 and 8 only")
    print(place_boat(board))
    if y > 8 or y < 0:
      print("Enter co-ordinates between 1 and 8 only")
    print(place_boat(board))
  else:
      if board[x][y] == " ":
      #places boat
        board[x][y] = "b"
        return " "
      else:
        #if the [osition is taken then this is used. The function is re-run with a message to the user
        print("This co-ordinate is taken")
        print(place_boat(board))
        return " "
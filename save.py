#For saving the game
def save_game():
  from board1 import board
  from board2 import board_2
  ####################################
  #Takes a 2D list of integers, creates a new 2D list with the same values as the string data type, joins the 2D list into a string with a comma between each item and a new line between each row. Writes the single string to a CSV file. 
  str_number_grid = []
  for item in board:
    row = []
    for number in item:
        row.append(str(number))
    str_number_grid.append(row)
  data = ""

  for x in range(0, 9):
      data = data + ",".join(str_number_grid[x]) + "\n"
  
  file = open("board1saved.csv", "w")
  file.write(data)
  file.close()
  #########################################
  #same for this one, but saves ai's boat positions
  str_number_grid2 = []
  for item2 in board_2:
    row2 = []
    for number2 in item2:
        row2.append(str(number2))
    str_number_grid2.append(row2)
  data2 = ""

  for x2 in range(0, 9):
      data2 = data2 + ",".join(str_number_grid2[x2]) + "\n"
  
  file = open("board2saved.csv", "w")
  file.write(data2)
  file.close()

save = False
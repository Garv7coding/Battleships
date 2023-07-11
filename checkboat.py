#Checks co-ordinates for human player's input
def checkcoords():
	from board1 import board
	from board2 import board_2
	from display import disboard
	from display import displayboard
	from display import displayboard2
	from save import save_game
	from quit import quit
	save_game()
    #print(quit())

	x = int(input("Enter X coordinate for boat guess:   "))
	y = int(input("Enter y coordinate for boat guess:  "))
	#checks if input is correct
	if x > 8 or x < 0:
	  print("Enter co-ordinates between 1 and 8 only")
	  print(checkcoords())
	if y > 8 or y < 0:
	  print("Enter co-ordinates between 1 and 8 only")
	  print(checkcoords())
		#it can only be a hit or a miss
		#checks if input is a correct guess for boat or not
	if board_2[x][y] == " ":  
	  disboard[x][y] = "M"
	  print("you missed!")
	  print(displayboard2(disboard))
	  return " "
		#if the boat is hit by the enemy or not
	if board_2[x][y] == "b":
		print("hit!")
		disboard[x][y] = "H"
		print(displayboard2(disboard))
		return " "
       
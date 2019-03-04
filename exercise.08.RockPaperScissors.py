accList = ["Y","y","N","n"]
print("We're playing Rock Paper Scissors!")
while True:
	
	player1 = 0
	player2 = 0
	while not player1 in range(1,4):
		player1 = int(input("Player one, pick your weapon:\n1: Rock\n2: Paper\n3: Scissor\n"))
	while not player2 in range(1,4):
		player2 = int(input("Player two, pick your weapon:\n1: Rock\n2: Paper\n3: Scissor\n"))
	
	if player1 == player2:
		print("The game is a draw")
	elif (player2==2 and player1==1) or (player2==3 and player1==2) or (player2==1 and player1==3):
		print("Player 1 has won")
	elif (player1==2 and player2==1) or (player1==3 and player2==2) or (player1==1 and player2==3):
		print("Player 2 has won")
	
	playAgain = ""
	while not playAgain in accList:
		playAgain = input("Do you want to play again\ny/n\n")
	if playAgain == "y" or playAgain == "Y":
		continue
	if playAgain == "n" or playAgain == "N":
		break
import random
guessN = random.randint(1,10)
userInput = None
counter = 0
corrcount = 0
print("Guess a number between 1 and 10, or type exit to exit!\n")
while userInput != guessN and userInput != 'exit':
	userInput = input("")
	if userInput == 'exit':
		break
	userInput = int(userInput)
	if userInput == guessN:
		print("You guess the correct number! Let's try again!")
		corrcount +=1
		userInput = None
		guessN = random.randint(1,10)
	elif userInput < guessN:
		print("The number i'm thinking of is higher!")
	elif userInput > guessN:
		print("The number i'm thinking of is lower!")
	counter +=1
print("You've decided you're done playing, and you guessed {} times, out of which {} were correct!".format(counter, corrcount))

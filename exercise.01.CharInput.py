userName = input("What is your name?\n")
userAge = int(input("And how old are you?\n"))
pTimes = int(input("How many times do you wish me to print my greeting?\n"))
for i in range(pTimes):
		print("Greeting number {}:\n Dear {}, in {} years you'll be 100 years old!\n"
		.format(i+1, userName, 100-userAge))
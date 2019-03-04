inNum = int(input("Input a number, and i'll tell you whether it's odd or even\n"))

if inNum%4 == 0:
	print("{} is a multiple of 4, WAOW!".format(inNum))
elif inNum%2 == 0:
	print("{} is an even number!".format(inNum))
else:
	print("{} is an odd number!".format(inNum))

newNum = int(input("Now let's see if 2 integers divide evenly, what is your first integer?\n"))
divident = int(input("And your second integer?\n"))
if newNum%divident == 0:
	print("{}/{} does indeed divide evenly!".format(newNum, divident))
else:
	print("{}/{} does not divide evenly, it has the remainder {}.".format(newNum, divident, newNum%divident))
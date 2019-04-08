#The user inputs a number, and we check if it's a prime
def get_Prime(stringOut):
	return int(input(stringOut))
checkFlag = True
primeNum = get_Prime("Input an integer, and i will check whether said integer is a primenumber\n")
for i in range(2, primeNum):
	if primeNum%i == 0:
		print("{} is ufortunately not a prime number, as it is divisible by {}".format(primeNum, i))
		checkFlag = False
if checkFlag:
	print("{} is a prime number as it is only divisable by 1 and itself".format(primeNum))
	
	
input()
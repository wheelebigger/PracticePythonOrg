divNum = int(input("Type in a number, and i'll tell you the divisors of that number\n"))

# for i in range(divNum):
	# if divNum%(i+1) == 0:
		# print("{} divided by {} leaves a remainder of 0 and thus is a divisor of {}"
		# .format(divNum, i+1, divNum))

# for i in range(1, divNum+1):
	# if divNum%i == 0:
		# print("{} divided by {} leaves a remainder of 0 and thus is a divisor of {}"
		# .format(divNum, i, divNum))

divList = []		
for i in range(1, divNum+1):
	if divNum%i == 0:
		divList.append(i)
print(divList," are all divisors of {}".format(divNum))
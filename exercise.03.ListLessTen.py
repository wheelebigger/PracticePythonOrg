#A program which prints out all the elements of a list, which are less than ten
tenList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in range(len(tenList)):
	# if tenList[i] < 10:
		# print("{}, is less than ten".format(tenList[i]))

# newList = []
# for i in range(len(tenList)):
	# if tenList[i] < 10:
		# newList.append(tenList[i])
# print(newList)

# newList = [i for i in tenList if i < 10]
# print(newList)

testNum = int(input("Give us a number, and i'll tell you which numbers from the list are lower\n"))
tList = [i for i in tenList if i < testNum]
print("From\n{}\n{}\nare lower than {}".format(tenList, tList, testNum))
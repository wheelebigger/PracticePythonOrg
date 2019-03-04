# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.
# a = [5, 10, 15, 20, 25]
# newList = [a[0], a[-1]]
# print(newList)
a = [84, 829, 2, 64, 23, 64, 23, 43, 12, 5, 3, 6, 13]
def ListEnder(list):
	newList = [list[0], list[-1]]
	return newList

hello = ListEnder(a)
	
print(hello)

# def ListEnds(a):
# b = [a[x] for x in [0,-1]]
# return b
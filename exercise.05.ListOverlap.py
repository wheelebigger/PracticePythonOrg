#A program that checks for common elements between two lists
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# ab = []

# for i in range(b):
	# if b[i] in a:
		# ab.append(b[i])
# print(ab)
#Herfra har jeg googlet
import random
# a = []
# b = []
# for i in range(50):
	# a.append(random.randrange(0,100))
	# b.append(random.randrange(0,100))
# rList = [i for i in 50 append(random.randrange(0,100))]
a = random.sample(range(1,50),30)
b = random.sample(range(10,100),40)
abList = list(set(a)&set(b))
print(abList)
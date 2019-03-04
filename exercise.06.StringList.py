theString = input("Input a string, and i'll tell you whether what you wrote is a palindrome\n")
revString = ''.join(reversed(theString))
# print(revString)
if revString == theString:
# if theString[::-1] == theString:
	print(theString + " is in fact a palindrome!!!")
else:
	print(theString + " is not a palindrome :(")
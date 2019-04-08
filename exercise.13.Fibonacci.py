def Fibonacci(x):
	c = []
	a, b = 0, 1
	for i in range(x+1):
		if i != 0:
			c.append(a)
		a, b = b, a + b
	return c

loopy = int(input("I can cycle through the fibonaccinumbers for you - how many numbers do you want me to print?\n"))
print('\n')
FibList = Fibonacci(loopy)
print(FibList)

input()
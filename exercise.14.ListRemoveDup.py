a = [10, 20, 30, 10, 40, 50, 30, 70, 100, 80, 20, 90, 60]

def RemoveSet(x):
	newList = sorted(set(x))
	return newList

def RemoveLoop(x):
	newList = []
	for i in range(len(x)):
		if x[i] not in newList:
			newList.append(x[i])
	return sorted(newList)
dupli = RemoveLoop(a)
print(dupli)
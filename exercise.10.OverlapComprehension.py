#Using list comprehension, combine the overlaps of two lists into a a new list.
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#print([i for i in a if i in b]) 
#print(list(set(a)&set(b)))

#opgave 2
import random
print([i for i in random.sample(range(1,50),30) if i in random.sample(range(10,100),40)])
#eller
print(list(set(random.sample(range(1,50),30))&set(random.sample(range(10,100),40))))
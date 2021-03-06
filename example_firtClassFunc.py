'''
Lets assume we have the following data
'''

year_cheese = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003,
30.66),(2004, 31.33), (2005, 32.62), (2006, 32.73), (2007, 33.5),
(2008, 32.84), (2009, 33.02), (2010, 32.92)]



'''
If we say:
'''
result = max(year_cheese)
print(result)

'''
We are going to get a tuple of 2 orderd by the element on the 0 place of the tuple
'''

'''
If we would like to get our order to be taken place after
the second element we need to use the higher order feature 
of the max function
'''

res2 = max(year_cheese, key=lambda year_cheese: year_cheese[1])
print(res2)

'''
If we def the lambda outside:
'''

def key1(self):
	return self[1]

res3 = max(year_cheese, key=key1)
print(res3)

'''
If we would like to get the highest element on [1] position
and the whole tuple of that element
'''
GetMaxTuple = max(map(lambda yc: (yc[1], yc), year_cheese))
print(GetMaxTuple)
'''
OR
'''
def key1__01(self):
	return self[1], self 

GetMaxTupleWithFunction = max(map(key1__01, year_cheese))
print(GetMaxTupleWithFunction)

'''
Ofc we can say
'''
GetSecondElementOfMaxTuple = max(map(key1__01, year_cheese))[1]
print(GetSecondElementOfMaxTuple)

'''
However
max(map(key1__01, year_cheese)) is an object NOT a function in my view point
so i would do
'''
print(GetMaxTupleWithFunction[1])

'''
More times
'''


'''
Or even something like
'''

GetSecondElementOfMaxTuple_version_2 = GetMaxTupleWithFunction[1]
print(GetSecondElementOfMaxTuple_version_2)

'''
The nameing is not conventional i know, but
giving an other name for an other object is much 
"cleaner" (from clean code) for me...
'''
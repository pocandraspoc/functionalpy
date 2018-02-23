import math
import os

def IsPrime(number):
	def inner_IsPrime(k, coprime):
		"""
		Is K relatively prime to the value coprime?
		"""
		if k < coprime *coprime:
			return True
		if k % coprime == 0:
			return False
		return inner_IsPrime(k, coprime+2)
	if number < 2:
		return False
	if number == 2:
		return True
	if number % 2 == 0:
		return False
	return inner_IsPrime(number, 3)

def IsBiggerPrime(number):
	if number < 2:
		return False
	if number == 2:
		return True
	if number % 2 == 0:
		return False
	return not any(number==0 for number in range(3, int(math.sqrt(number))+1 , 2))

"""
result = IsPrime(15)
print(result)

print(2**0.5)
MayPrime = (2**61)-1
res2 = IsBiggerPrime(MayPrime)
print("There")
"""
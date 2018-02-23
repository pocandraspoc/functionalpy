import collections
import AACprime

class Mesennel(collections.Callable):
	def __init__(self, algorithm):
		self.pow2= algorithm
	def __call__(self, arg):
		return self.pow2(arg)-1

def shity(power):
	return 1 << power
def multy(power):
	if power == 0:
		return 1
	return 2*multy(power-1)
def faster(power):
	if power == 0:
		return 1
	if power%2 ==1:
		return 2*faster(power-1)
	t= faster(power//2)
	return t*t

m1s=Mesennel(shity)
mlm=Mesennel(multy)
mlf=Mesennel(faster)

obj = mlf(2)
printable = obj
print(printable)

IsPrime = AACprime.IsBiggerPrime(obj)
printable = IsPrime
print(printable)


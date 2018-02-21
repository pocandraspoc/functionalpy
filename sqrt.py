def next_(n, x):
	return (x+ n/x)/2


def repeat(f, a):
	yield a 
	for v in repeat(f, f(a)):
		yield v

def headTail(e, a, iterable):
		b = next(iterable)
		if abs(a-b) <= e:
			return b
		return headTail(e, b, iterable)

def within(e, iterable):
	return headTail(e, next(iterable), iterable)


def sqrt(a0, e, n):
	return within(e, repeat(lambda x: next_(n,x), a0))
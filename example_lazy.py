def numbers():
	for index in range(1024):
		print("=", index)
		yield index


def SumTo(number):
	sum= 0
	for index in numbers():
		if index == number:
			break
		sum += index
	return sum

print(SumTo(5))

'''
this small game is a good way to understand lazy
at the other hand
it is extremly dangerous to hardcode the
'1024'
in the first example!!!!
'''
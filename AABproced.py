def proc(LowerB, UpperB):
	index = 0
	for n in range(LowerB, UpperB):
		if n % 3 == 0 or n % 5 == 0:
			index += n
	return index

print(proc(1,20))
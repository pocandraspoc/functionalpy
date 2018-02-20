def proc(LowerB, UpperB):
	List = list()
	for n in range(LowerB, UpperB):
		if n % 3 == 0 or n % 5 == 0:
			List.append(n)
	SumList = sum(List)
	return SumList

print(proc(1,15))
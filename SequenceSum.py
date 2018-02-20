def suming(seq):
	if len(seq) == 0: return 0
	return seq[0] + sum(seq[1:])

#print(suming([1,2,3]))

def until(n, filter_func, v):
	if v == n: return []
	if filter_func(v): return [v] + until(n, filter_func, v+1)
	else: return until(n, filter_func, v+1)

mult_3_5 = lambda x: x%3==0 or x%5==0

print(mult_3_5(19))
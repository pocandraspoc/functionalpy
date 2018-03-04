import sys
print("Starting to solve: https://www.hackerrank.com/challenges/plus-minus/problem")

def plusMinus(ar):
	preCountPlus = 0
	preCountMinus = 0
	preCountZero = 0
	longAr = len(ar)
	for index in range(len(ar)):
		if ar[index] == 0:
			preCountZero = preCountZero + 1
		elif ar[index] > 0:
			preCountPlus = preCountPlus + 1
		else:
			preCountMinus = preCountMinus +1
	listOut = [preCountPlus/longAr, preCountMinus/longAr, preCountZero/longAr]
	return print(listOut)

def plusSecondMinus(arr, n):
    n = n 
    lst = arr
    print(format(len([x for x in lst if x > 0])/n, ".10f"))
    print(format(len([x for x in lst if x < 0])/n, ".10f"))
    print(format(len([x for x in lst if x == 0])/n, ".10f"))


#n = int(input().strip())
#ar = list(map(int, input().strip().split(' ')))
ar = [-4, 3, -9, 0, 4, 1]
n = len(ar)

plusMinus(ar)
plusSecondMinus(ar, n)

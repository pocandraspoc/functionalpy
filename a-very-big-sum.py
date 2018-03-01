#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    preSum = 0
    for index in range(n):
    	preSum += ar[index]
    return preSum

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)

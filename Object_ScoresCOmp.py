#!/bin/python3

import sys
def solve(a0, a1, a2, b0, b1, b2):
    inp_a=[a0,a1,a2]
    inp_b=[b0,b1,b2]
    res_a=0
    res_b=0
    for index in range(3):
        if inp_a[index]>inp_b[index]:
            res_a = res_a + 1
            res_b = res_b
        elif inp_a[index]<inp_b[index]:
            res_a = res_a
            res_b = res_b + 1
        else:
        	pass
    return [res_a, res_b]

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
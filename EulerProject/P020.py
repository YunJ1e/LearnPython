"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/29
Author: Yunjie Wang
"""

"""
Problem 20 (648)
"""
import math

def func020():
	fac = math.factorial(100)
	res = 0
	for digit in str(fac):
		res += int(digit)
	return res

print(func020())
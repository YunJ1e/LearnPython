"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/04
Author: Yunjie Wang
"""

"""
Problem 34 (40730)
"""
import math

def func034():
	res = 0
	for i in range(3, 10**7):
		num = 0
		for str_digit in str(i):
			num += math.factorial(int(str_digit))
		if num == i:
			res += num
	print(res)

func034()
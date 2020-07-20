"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/19
Author: Yunjie Wang
"""

"""
Problem 2 (4613732)
"""

import math

def func002():
	upper_limit = 4000000
	x = 1
	y = 2
	sum = 0
	while x <= upper_limit:
		if x % 2 == 0:
			sum += x
		temp = y
		y = x + y
		x = temp
	print(sum)
# func002()
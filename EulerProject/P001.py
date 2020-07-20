"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/19
Author: Yunjie Wang
"""

"""
Problem 1 (233168)
"""

import math

def func001():
	res = 0
	for i in range(1, 1000):
		if (i % 3) == 0 or (i % 5) == 0:
			res += i
	print(res)
# func001()
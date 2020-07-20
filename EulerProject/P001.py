"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/19
Author: Yunjie Wang
"""

import math
"""
Problem 1 (233168)
"""
def func001():
	target_list = []
	for i in range(1, 1000):
		if (i % 3) == 0 or (i % 5) == 0:
			target_list.append(i)
	result = sum(target_list)
	print(result)
# func001()
"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/03
Author: Yunjie Wang
"""

"""
Problem 32 (45228)
"""

import math

def is_usual(num):
	for i in range(1, int(math.sqrt(num)) + 1, 1):
		if num % i == 0:
			multiplier = num // i
			aString = "".join(sorted(list(str(num) + str(i) + str(multiplier))))
			if aString == "123456789":
				return True
	return False

def func032():
	res_list = []
	for num in range(1, 10000):
		if is_usual(num):
			res_list.append(num)
	print(sum(res_list))

func032()
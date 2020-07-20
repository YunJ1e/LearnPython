"""
Euler Project
Updated: 2020/07/20
Author: Yunjie Wang
"""

import math
"""
Problem 6 (25164150)
"""

def sum_of_square(n):
	"""
	:param n: The first n number
	:return:
	"""
	return sum([i*i for i in range(1, n+1)])

def sum_of_first_n(n):
	"""
	:param n:
	:return:
	"""
	return sum([i for i in range(1, n+1)])

def difference(n):
	"""

	:param n:
	:return:
	"""
	return -sum_of_square(n) + sum_of_first_n(n)**2

# print(difference(100))
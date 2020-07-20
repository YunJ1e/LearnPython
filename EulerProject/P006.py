"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/20
Author: Yunjie Wang
"""

"""
Problem 6 (25164150)
"""

import math

def sum_of_square(n):
	"""
	:param n: The first n number
	:return: The sum of square of the first n numbers
	"""
	return sum([i*i for i in range(1, n+1)])

def sum_of_first_n(n):
	"""
	:param n: The first n number
	:return: The sum of the first n numbers
	"""
	return sum([i for i in range(1, n+1)])

def difference(n):
	"""
	:param n: The first n number
	:return: The difference between the sum of the squares and the square of the sum
	"""
	return - sum_of_square(n) + sum_of_first_n(n)**2

def func006():
	print(difference(100))
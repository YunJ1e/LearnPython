"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/20
Author: Yunjie Wang
"""

"""
Problem 7 (104743)
"""

import math

def is_prime(num):
	"""
	Function: Determine whether the input number is prime or not
	:param num:
	:return: True if the number is prime, otherwise False
	"""
	# Check whether or not it can be divided by the 2 ans some corner cases
	# By definition, 1 is not a prime number
	if num == 1:
		return False
	if num == 2:
		return True
	if num % 2 == 0:
		return False
	# The number for sure is a odd one from now
	for i in range(3, num, 2):
		if num % i == 0:
			return False
	return True

def func007():
	counter = 0
	i = 0
	while counter < 10001:
		i += 1
		if is_prime(i):
			counter += 1

	print(i)

func007()
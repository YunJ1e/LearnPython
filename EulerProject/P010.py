"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/21
Author: Yunjie Wang
"""

"""
Problem 10 ()
"""

import math

def is_prime(num):
	if num == 1:
		return False
	if num == 2:
		return True
	if num % 2 == 0:
		return False
	for i in range(3, int(math.sqrt(num)) + 1, 2):
		if num % i == 0:
			return False

	return True

def sum_all_primes(numBound):
	# Calculate the sum of the primes before numBound
	res = 0
	for i in range(1, numBound + 1):
		if is_prime(i):
			# print(i)
			res += i
	return res

print(sum_all_primes(2000000))
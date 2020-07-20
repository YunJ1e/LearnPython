"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/19
Author: Yunjie Wang
"""

"""
Problem 3 (6857)
"""

import math

def max_prime_factor(num):
	max_prime = -1
	# The largest possible factor
	sqrt_num = int(math.sqrt(num))

	# If the number is divisible only by 2,
	# the result will be 2.
	# Otherwise it will break out the while loop
	# And the num right now cannot be divided by 2 any more
	while num % 2 == 0:
		max_prime = 2
		num = num // 2
	# The possible factor start from 3, end at sqrt_num
	# because the num cannot be divided by 2 any more, choose step to be 2
	for i in range(3, sqrt_num + 1, 2):
		while num % i == 0:
			max_prime = i
			num = num // i
	if num > max_prime:
		max_prime = num

	return max_prime
# print(max_prime_factor(600851475143))
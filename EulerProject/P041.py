"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/20
Author: Yunjie Wang
"""
from itertools import permutations
"""
Problem 41 (7652413)

Analysis: An n-digit number is pandigital if it makes use of all the digits 1 to n exactly once
If n is greater than 10, and all the digits have to be used once, the number will at least have 11 digits.
And this contradicts the fact that it is a n-digit number.
Since the largest possible pandigital number is 987654321, we could start from here and look for prime.
"""


def compute():
	num = 123456789
	num_list = list(str(num))
	while True:
		perm = permutations(num_list)
		for i in sorted(list(perm), reverse=True):
			num = int("".join(i))
			if is_prime(num):
				return num
		num_list.pop()



def is_prime(num):
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

print(compute())
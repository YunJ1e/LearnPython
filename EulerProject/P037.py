"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/05
Author: Yunjie Wang
"""

"""
Problem 37 (748317)
"""

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

def is_truncate_prime(num):
	for i in range(len(str(num))):
		if not is_prime(int(str(num)[i:])):
			return False
	return True

def is_truncate_prime_reverse(num):
	for i in range(len(str(num)), 0, -1):
		if not is_prime(int(str(num)[:i])):
			return False
	return True


def func037():
	count = 0
	i = 11
	res = 0
	while count < 11:
		if is_truncate_prime(i) and is_truncate_prime_reverse(i):
			count += 1
			res += i
			print(i)
		i += 1
	print(res)

func037()
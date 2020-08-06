"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/05
Author: Yunjie Wang
"""

"""
Problem 35 (55)
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

def circular_num(num):
	num_list = []
	num = str(num)
	for i in range(len(num)):
		if not is_prime(int(num[i:]+num[:i])):
			return False
			# num_list.append(int(num[i:]+num[:i]))
	return True

def smallest_circular(num):
	num_list = []
	num = str(num)
	for i in range(len(num)):
		num_list.append(int(num[i:]+num[:i]))
	return min(num_list), len(set(num_list))

# print(smallest_circular(11))
def func035():
	count = 0
	for i in range(1, 1000001):
		min_num, num_count = smallest_circular(i)
		if i == min_num:
			if circular_num(i):
				# print(i, num_count)
				count += num_count
	print(count)

func035()
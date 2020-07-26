"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/26
Author: Yunjie Wang
"""

"""
Problem 12 (76576500)
"""

# For a number that has over 500 divisors, its square root has to be greater than 250
# 1. Every divisors appear in pairs(except 1 itself 1 = 1)
# 2. 250 * 250 = 62500
import math

def triangular_num(num_list, index):
	# There is a mismatch in the index of the list and the index of the triangular number index
	# So I need to plus after every index
	# The n-th triangular number actually the (n-1)th in the list, eg. the first triangular number is the 0-th in the list
	real_index = index - 1
	if index == 1 or len(num_list) == 0:
		num_list.append(index)
	else:
		num_list.append(index + num_list[real_index - 1])
	return num_list[-1]

def calculate_triangle_num():
	num_list = []
	num = -1
	i = 0
	num_of_divisor = 0
	while num_of_divisor <= 500:
		i += 1
		num = triangular_num(num_list, i)
		num_of_divisor =  count_divisor(num)
	return num

def count_divisor(num):
	count = 2
	if num == 1:
		return 1
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			# The number is divisible
			if num / i == i:
				count += 1
			else:
				count += 2
	return count

def func012():
	res = calculate_triangle_num()
	print(res)

func012()
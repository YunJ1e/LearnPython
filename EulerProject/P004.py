"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/19
Author: Yunjie Wang
"""

"""
Problem 4 (906609)
"""

import math

def number_list(num):
	digit_list = []
	while num != 0:
		digit_list.append(num % 10)
		num = num // 10
	return digit_list

def reverse_num(num):
	nums_list = number_list(num)
	list_length = len(nums_list)
	result = 0
	for i in range(list_length):
		result += nums_list[list_length - i - 1] * (10 ** i)
	return result

def max_palindrome_product(ndigit):
	# using string manipulation would be easier than complete number operation
	# The number range of that digit
	lower_bound = 10**(int(ndigit) - 1)
	upper_bound = 10**(int(ndigit)) - 1
	result = 0
	for i in range(upper_bound, lower_bound - 1, -1):
		for j in range(upper_bound, lower_bound - 1, -1):
			product_result = i * j
			mirror_result = reverse_num(product_result)
			if mirror_result == product_result and product_result > result:
				result = product_result
	return result
# print(max_palindrome_product(3))
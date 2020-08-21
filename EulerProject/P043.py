"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/21
Author: Yunjie Wang
"""
from itertools import permutations
"""
Problem 43 (16695334890)
In this problem, the first number could be 0, but we do not have to care about that because the check is from second digit
"""


def compute():
	sum = 0
	# num(a list) will be the permutations of 0~9
	for num in permutations(list(range(10))):
		# print(num)
		if is_divisible_property(num):
			for digit_index in range(len(num)):
				sum += num[digit_index] * 10 **(len(num) - digit_index - 1)
	print(sum)


def is_divisible_property(num):
	check_list = [2, 3, 5, 7, 11, 13, 17]
	for digit_index in range(3, len(num)):
		temp_num = num[digit_index - 2] * 100 + num[digit_index - 1] * 10 + num[digit_index]
		if temp_num % check_list[digit_index - 3]:
			return False
	return True


compute()
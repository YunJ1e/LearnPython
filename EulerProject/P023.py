"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/30
Author: Yunjie Wang
"""

"""
Problem 23 (4179871)
"""
# We know that every number that is greater than this can be expressed by the sum of two abundant numbers
LIMIT = 28123

def sum_of_divisor(N=LIMIT+1):
	# From this, we know the sum of the proper divisor for each position
	aList = [0] * N
	for i in range(1, N):
		for j in range(i * 2, N, i):
			aList[j] += i
	# print(aList)
	return aList

def is_abundant(num_list):
	# Get every abundant number(index)
	bool_list = [False] * len(num_list)
	for i in range(len(num_list)):
		if num_list[i] > i:
			bool_list[i] = True
	return bool_list

def sum_of_two_abundant(bool_list):
	sum_bool_list = [False] * len(bool_list)
	for i in range(len(bool_list)):
		for j in range(len(bool_list)):
			if i + j < len(bool_list) and bool_list[i] and bool_list[j]:
				sum_bool_list[i + j] = True
	return sum_bool_list

def sum_of_non_abundant():
	alist = sum_of_two_abundant(is_abundant(sum_of_divisor()))
	res = 0
	for i in range(len(alist)):
		if alist[i] == False:
			res += i
	print(res)

sum_of_non_abundant()
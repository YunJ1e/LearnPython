"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/05
Author: Yunjie Wang
"""

"""
Problem 36 (872187)
"""

def is_palindromes(num):
	if str(num) == str(num)[::-1] and bin(num).replace("0b", "") == bin(num).replace("0b", "")[::-1]:
		return True
	else:
		return False

def func036():
	sum_res = 0
	for i in range(0, 10**6 + 1):
		if is_palindromes(i):
			sum_res += i
	print(sum_res)

func036()
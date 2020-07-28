"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/28
Author: Yunjie Wang
"""

"""
Problem 16 (1366)
"""

def func016():
	sum = 0
	res = list(str(2**1000))
	for num in res:
		sum += int(num)
	print(sum)

func016()
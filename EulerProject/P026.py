"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/31
Author: Yunjie Wang
"""

"""
Problem 26 (982)
"""
import itertools

def pattern(n):
	seen = {}
	x = 1
	for i in itertools.count():
		if x in seen:
			return i - seen[x]
		else:
			seen[x] = i
			x = x * 10 % n

def func026():
	max_len = 0
	for i in range(1, 1001):
		max_len = max(max_len, pattern(i))
	print(max_len)

func026()
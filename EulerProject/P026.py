"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/31
Author: Yunjie Wang
"""

"""
Problem 26 ()
"""
import itertools

def compute():
	ans = reciprocal_cycle_len(4)
	return str(ans)


def reciprocal_cycle_len(n):
	seen = {}
	x = 1
	for i in itertools.count():

		if x in seen:
			return i - seen[x]
		else:
			print(x)
			seen[x] = i
			x = x * 10 % n
print(compute())
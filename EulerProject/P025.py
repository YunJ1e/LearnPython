"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/31
Author: Yunjie Wang
"""

"""
Problem 25 (4782)
"""

def fib():
	LIMIT = 1000
	fib_list = []
	fib_list.append(0)
	fib_list.append(1)
	i = 2
	while len(str(fib_list[i - 1])) < LIMIT:
		fib_list.append(fib_list[i - 1] + fib_list[i - 2])
		print(i)
		i += 1

fib()
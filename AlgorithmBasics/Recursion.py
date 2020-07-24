"""
Updated: 2020/07/23
Author: Yunjie Wang
"""

"""
Recursion
"""

def loop_fib(n):
	# The function is to calculate the n-th fibonacci number
	# By definition, the fibonacci numbers are 0, 1, 1, 2, 3, 5 etc
	if n <= 1:
		return n
	a = 0
	b = 1
	for i in range(1, n):
		temp = b
		b += a
		a = temp
	return b

def recur_fib(n):
	if n <= 1:
		return n
	return recur_fib(n - 1) + recur_fib(n - 2)

# for i in range(10):
# 	print(loop_fib(i))
#
# 	print(recur_fib(i))
# 	print("---------------------")
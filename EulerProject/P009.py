"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/22
Author: Yunjie Wang
"""

"""
Problem 9 (31875000)
"""

# a + b + c = 1000
# a < b < c
# So the lower bound for a is 1, upper point for a is 332
def func009():
	sum = 1000
	for a in range(1, sum):
		for b in range(a + 1, sum):
			if a*a + b*b == (sum - a - b)*(sum - a - b):
				return a, b, sum-a-b


x, y, z = func009()
print(x*y*z)
"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/19
Author: Yunjie Wang
"""

import math
"""
Problem 5(232792560)
"""
def least_comment_multiplier(n):
	result = 1
	for i in range(1, n+1):
		result = int(result * i / math.gcd(result, i))
	return result
# print(least_comment_multiplier(20))
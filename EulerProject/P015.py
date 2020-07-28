"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/28
Author: Yunjie Wang
"""

"""
Problem 15 (137846528820)
"""

import math

def n_choose_k(n, k):
	# n must not less than k
	return int(math.factorial(n)/(math.factorial(k) * math.factorial(n - k)))

def func015():
	hori_grid = 20
	vert_grid = 20
	print(n_choose_k(hori_grid+vert_grid, hori_grid))

func015()
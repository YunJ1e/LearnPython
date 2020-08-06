"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/05
Author: Yunjie Wang
"""

"""
Problem 38 (840)
"""

def is_right_triangle(x, y, z):
	return x ** 2 + y ** 2 == z ** 2

def right_triangle_sum(SUM):
	result = 0
	for x in range(1, SUM):
		for y in range(x, (SUM - x) // 2 + 1):
			z = SUM - x - y
			if is_right_triangle(x, y, z):
				result += 1
	return result

def func039():
	max_res = -1
	max_index = 0
	for i in range(1, 1000):
		if right_triangle_sum(i) > max_res:
			max_res = right_triangle_sum(i)
			max_index = i
	print(max_index)

func039()
"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/30
Author: Yunjie Wang
"""

"""
Problem 24 (2783915460)
"""
from itertools import permutations
def func024():
	mill_list = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
	res = ""
	for num in mill_list[999999]:
		res += str(num)

	print(res)
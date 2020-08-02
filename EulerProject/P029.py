"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/02
Author: Yunjie Wang
"""

"""
Problem 29 (9183)
"""

def func029():
	target_list = []
	for i in range(2, 101):
		for j in range(2, 101):
			target_list.append(i ** j)
	target_set = set(target_list)
	return len(target_set)

print(func029())
"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/29
Author: Yunjie Wang
"""

"""
Problem 19 (171)
"""

import datetime

def func019():
	ans = sum(1
		for year in range(1901, 2001)
		for month in range(1, 13)
		if datetime.date(year, month, 1).weekday() == 6)
	return ans

print(func019())
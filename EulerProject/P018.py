"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/29
Author: Yunjie Wang
"""

"""
Problem 18 (1074)
"""
import math

def get_number(aMatrix, row_index, col_index):
	try:
		return aMatrix[row_index][col_index]
	except IndexError:
		return -math.inf

def get_max(num01, num02):
	return max(num01, num02)

def triangle_cal():
	triangle = [
		[75],
		[95, 64],
		[17, 47, 82],
		[18, 35, 87, 10],
		[20, 4, 82, 47, 65],
		[19, 1, 23, 75, 3, 34],
		[88, 2, 77, 73, 7, 63, 67],
		[99, 65, 4, 28, 6, 16, 70, 92],
		[41, 41, 26, 56, 83, 40, 80, 70, 33],
		[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
		[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
		[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
		[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
		[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
		[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
	]
	row = len(triangle)
	add_num = []
	for row_index in range(row - 1, 0, -1):
		for col_index in range(len(triangle[row_index])):
			add_num.append(get_max(get_number(triangle, row_index, col_index), get_number(triangle, row_index, col_index + 1)))
		for i in range(len(triangle[row_index - 1])):
			triangle[row_index - 1][i] += add_num[i]
		add_num = []
	print(triangle[0])

triangle_cal()


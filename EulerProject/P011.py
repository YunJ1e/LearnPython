"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/24
Author: Yunjie Wang
"""

"""
Problem 11 ()
"""

def sum_all_direction(x_index, y_index, x_matrix, y_matrix):
	pass

def get_number(matrix_input, x_index, y_index):
	# Assume there is a valid input of rhe matrix
	# If the index input is not valid, return None instead
	if x_index not in range(len(matrix_input)) or y_index not in range(len(matrix_input[0])):
		return None
	else:
		return matrix_input[x_index][y_index]

print(get_number([[1,2],[3,4]], -1,1))



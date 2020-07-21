"""
Binary Search Problems
Updated: 2020/07/20
Author: Yunjie Wang
"""
"""
Given a 2D matrix that contains integers only, which each row is sorted in an ascending order. 
The first element of next row is larger than (or equal to) the last element of previous row.
Given a target number, returning the position that the target locates within the matrix.
If the target number does not exist in the matrix, return {-1, -1}.

Assumptions:
The given matrix is not null, and has size of N * M, where N >= 0 and M >= 0.
Examples:
matrix = { {1, 2, 3}, {4, 5, 7}, {8, 9, 10} }
target = 7, return {1, 2}
target = 6, return {-1, -1} to represent the target number does not exist in the matrix.
"""

def binary_search_in_2D(aMatrix, target):
	if len(aMatrix) == 0 and len(aMatrix[0]) == 0:
		return (-1, -1)

	row = len(aMatrix)
	col = len(aMatrix[0])
	left = 0
	right = row * col - 1
	while left <= right:
		mid = (left + right) // 2
		row_mid = mid // row
		col_mid = mid % row
		if aMatrix[row_mid][col_mid] < target:
			left = mid + 1
		elif aMatrix[row_mid][col_mid] > target:
			right = mid - 1
		else:
			return (row_mid, col_mid)
	return (-1, -1)

# print(binary_search_in_2D([[1,2,3], [4,5,7],[8,9,10]], 6))

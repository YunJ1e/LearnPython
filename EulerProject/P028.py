"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/01
Author: Yunjie Wang
"""

"""
Problem 28 (669171001)
"""
# def change_around_index(ori_matrix, ori_x, ori_y, dx, dy, value):
# 	ori_matrix[ori_x + dx][ori_y + dy] = value
#
# def spiral_matrix(row_para, col_para):
# 	if row_para <= 0 or col_para <= 0:
# 		return
# 	if row_para % 2 == 0 or col_para % 2 == 0:
# 		return
# 	aMatrix = [ [ 0 for i in range(col_para) ] for j in range(row_para) ]
# 	aMatrix[row_para // 2][col_para // 2] = 1
# 	# center_index = row_para // 2, col_para // 2
# 	change_around_index(aMatrix, row_para // 2, col_para // 2, +1, +1, 20)
#
# 	for i in range(len(aMatrix)):
# 		print(aMatrix[i])


# 11 x 11 matrix
def func():
	res = 1
	dif = 1
	for acc in range(2, 1002, 2):
		for i in range(4):
			dif = acc + dif
			res = res + dif
			print(dif, res)

func()
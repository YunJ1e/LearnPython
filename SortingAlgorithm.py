"""
Updated: 2020/07/15
Author: Yunjie Wang
"""

def bubble_sort(list_to_sort):

	if not list_to_sort or len(list_to_sort) == 0:
		return
	# For Special case, len = 1, the outer for loop will not be execute
	# and nothing will be done on the list itself, nothing change
	for j in range(len(list_to_sort) - 1 , 0, -1):
		for i in range(j):
			if list_to_sort[i] > list_to_sort[i+1]:
				list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]
		# print(list_to_sort)
	return

a = [9,8,7,6,5,4,3,2,1]
bubble_sort(a)
print(a)
# for i in range(1, 1):
# 	print(111)
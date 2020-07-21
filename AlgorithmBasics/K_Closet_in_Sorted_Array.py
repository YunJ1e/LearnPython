"""
Binary Search Problems
Updated: 2020/07/20
Author: Yunjie Wang
"""
"""
Given a target integer T, a non-negative integer K and an integer array A sorted in ascending order, 
find the K closest numbers to T in A. 
If there is a tie, the smaller elements are always preferred.

Assumptions:
A is not null
K is guranteed to be >= 0 and K is guranteed to be <= A.length

Return:
A size K integer array containing the K closest numbers(not indices) in A, 
sorted in ascending order by the difference between the number and T.

Examples:
A = {1, 2, 3}, T = 2, K = 3, return {2, 1, 3} or {2, 3, 1}
A = {1, 4, 6, 8}, T = 3, K = 3, return {4, 1, 6}
"""

import AlgorithmBasics.SearchAlgorithm as SearchPackage

def k_closet_search(array, target, k):
	res = []
	if len(array) == 0 or k <= 0:
		return res
	# Find the closet number index(could be itself) ans store as a variable
	closet_index = SearchPackage.binary_search_closet_number(array, target)
	print(array[closet_index])
	res.append(array[closet_index])

	left = closet_index - 1
	right = closet_index + 1
	# This condition is to make sure the left and right index will not be out of index
	while k > 1 and (left >= 0 or right <= len(array) - 1):

		# It is possible that sometimes the left or right is out of index
		# but the k is not decreasing to 1
		k -= 1
		if (right <= len(array) - 1) and (left < 0 or
		                                    abs(array[left] - target) > abs(array[right] - target)):
			res.append(array[right])
			right += 1
		else:
			res.append(array[left])
			left -= 1
	return res

# print(k_closet_search([1,3,5,7], 4, 4))
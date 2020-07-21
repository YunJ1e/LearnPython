"""
Binary Search Problems
Updated: 2020/07/20
Author: Yunjie Wang
"""
"""
Given a target integer T and an integer array A sorted in ascending order, 
Find the total number of occurrences of T in A.
Examples
A = {1, 2, 3, 4, 5}, T = 3, return 1
A = {1, 2, 2, 2, 3}, T = 2, return 3
A = {1, 2, 2, 2, 3}, T = 4, return 0
Corner Cases
What if A is null? We should return 0 in this case.
"""

import AlgorithmBasics.SearchAlgorithm as SearchPackage

def total_occurrence(numList, target):
	first_occur_index = SearchPackage.binary_search_first_occurence(numList, target)
	counter = 0
	if not first_occur_index:
		return counter

	for i in range(first_occur_index, len(numList)):
		if numList[i] == target:
			counter += 1
		else:
			break
	return counter

# print(total_occurrence([1,2,2,2,3,3], 1))
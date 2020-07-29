"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/29
Author: Yunjie Wang
"""

"""
Problem 21 (31626)
"""

def sum_of_divisor(N):
	aList = [0] * N
	for i in range(1, N):
		for j in range(i * 2, N, i):
			aList[j] += i
	print(aList)
	return aList

def find_amicable_numbers(aList):
	res = 0
	for index in range(len(aList)):
		if aList[index] < len(aList) and aList[aList[index]] == index and aList[index] != index:
			res += aList[index]

find_amicable_numbers(sum_of_divisor(10000))


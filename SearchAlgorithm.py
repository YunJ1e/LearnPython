"""
Updated: 2020/07/13
Author: Yunjie Wang
"""

"""
Binary Search
1. Find target number in a sorted integer array
	* Assume the number is in the list for sure
2. Find an element in the array that is closet to the target number
	* The problem is slightly different, because we cannot automatically
	move mid to right or left by 1(mid could be the answer in this case)
	* The actual problem is to find the interval that surround the target
	number, the boundary could be the target number
"""


def binarySearch(numList, target):
	# If the number list is empty, return None representing (NOT FOUND)
	if not numList:
		return None
	# At first, set the left and right to the start and end index of the number list
	left = 0
	right = len(numList) - 1
	# Since we don't know how many times we need to run the loop, choose while loop
	# The ending case will be only one number and that one is not the number we want
	while left <= right:
		mid = (left+right) // 2
		# Successfully found and return the index of it
		if numList[mid] == target:
			return mid
		# The target is at the right side of the midpoint, we need to push the left to the (midpoint+1)
		elif numList[mid] < target:
			left = mid + 1 # The midpoint is for sure not the target, so we can start the "new" list from the next one
		# The target is at the left side of the midpoint, we need to push the right to the (midpoint+1)
		elif numList[mid] > target:
			right = mid - 1
	# Even the one last number is not the number we want, the target must not be in the number list
	return None


def binary_search_closet_number(numList, target):
	# If the number list is empty, return None representing (NOT FOUND)
	if not numList:
		return None
	# At first, set the left and right to the start and end index of the number list
	left = 0
	right = len(numList) - 1
	# Since we don't know how many times we need to run the loop, choose while loop
	# The ending case will be only one number and that one is not the number we want
	while left < right - 1:
		mid = (left + right) // 2
		# The target is at the right side of the midpoint, we need to push the left to the (midpoint)
		if numList[mid] < target:
			left = mid  # The midpoint is for sure not the target, so we can start the "new" list from the next one
		# The target is at the left side of the midpoint, we need to push the right to the (midpoint)
		elif numList[mid] > target:
			right = mid
		# Successfully found and return the index of it
		else:
			return mid
	# Even the one last number is not the number we want, the target must not be in the number list
	return left if(abs(numList[left]-target) <= abs(numList[right]-target)) else right

def binary_search_last_occurence(numList, target):
	# If the number list is empty, return None representing (NOT FOUND)
	if not numList:
		return None
	# At first, set the left and right to the start and end index of the number list
	left = 0
	right = len(numList) - 1
	# Since we don't know how many times we need to run the loop, choose while loop
	# The ending case will be only one number and that one is not the number we want
	while left < right - 1:
		mid = (left + right) // 2
		# The target is at the right side of the midpoint, we need to push the left to the (midpoint)
		if numList[mid] < target:
			left = mid + 1  # The midpoint is for sure not the target, so we can start the "new" list from the next one
		# The target is at the left side of the midpoint, we need to push the right to the (midpoint)
		elif numList[mid] > target:
			right = mid - 1
		# Successfully found and return the index of it
		else:
			left = mid
	if numList[right] == target:
		return right
	if numList[left] == target:
		return left

	return None

def binary_search_first_occurence(numList, target):
	# If the number list is empty, return None representing (NOT FOUND)
	if not numList:
		return None
	# At first, set the left and right to the start and end index of the number list
	left = 0
	right = len(numList) - 1
	# Since we don't know how many times we need to run the loop, choose while loop
	# The ending case will be only one number and that one is not the number we want
	while left < right - 1:
		mid = (left + right) // 2
		# The target is at the right side of the midpoint, we need to push the left to the (midpoint)
		if numList[mid] < target:
			left = mid + 1  # The midpoint is for sure not the target, so we can start the "new" list from the next one
		# The target is at the left side of the midpoint, we need to push the right to the (midpoint)
		elif numList[mid] > target:
			right = mid - 1
		# Successfully found and return the index of it
		else:
			right = mid
	if numList[left] == target:
		return left
	if numList[right] == target:
		return right

	return None
print(binary_search_first_occurence([1,3,3,3,3,4,5], 3))
print(binary_search_last_occurence([1,3,3,3,3,4,5], 3))






#Sample code for plotting
# import matplotlib.pyplot as plt
# probability = [0.3602150537634409, 0.42028985507246375,
#   0.373117033603708, 0.36813186813186816, 0.32517482517482516,
#   0.4175257731958763, 0.41025641025641024, 0.39408866995073893,
#   0.4143222506393862, 0.34, 0.391025641025641, 0.3130841121495327,
#   0.35398230088495575]
# names = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8', 'name9',
# 'name10', 'name11', 'name12', 'name13'] #sample names
# plt.bar(names, probability)
# # plt.xticks(names)
# # plt.yticks(probability) #This may be included or excluded as per need
# plt.xlabel('Names')
# plt.ylabel('Probability')
# plt.show()


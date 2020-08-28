"""
Updated: 2020/07/18
Author: Yunjie Wang
"""

from AlgorithmBasics import SearchAlgorithm


def bubble_sort(list_to_sort):
	"""
	The function sorts the list in the ascending order
	\nTime Complexity: O(n^2) n + (n - 1) + ... + 1 = n(n + 1)/2
	\nSpace Complexity: O(1) In-place Operation

	:param list_to_sort:
	:return: None
	"""
	if not list_to_sort or len(list_to_sort) == 0:
		return
	# For Special case, len = 1, the outer for loop will not be execute
	# and nothing will be done on the list itself, nothing change
	# Every outer for loop makes sure the number on j is greater than the numbers before it
	# By doing this, we can "bubble" the largest number from the first j numbers
	# And the inner loop guarantees that number on i is greater than the numbers before it
	for j in range(len(list_to_sort) - 1, 0, -1):
		for i in range(j):
			# As long as the next number is less than the current one, swap them
			if list_to_sort[i] > list_to_sort[i + 1]:
				list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
	return


def bubble_sort_reversed(list_to_sort):
	"""
	The function sorts the list in the descending order
	\nTime Complexity: O(n^2) n + (n - 1) + ... + 1 = n(n + 1)/2
	\nSpace Complexity: O(1) In-place Operation

	:param list_to_sort:
	:return: None
	"""
	if not list_to_sort or len(list_to_sort) == 0:
		return
	# For Special case, len = 1, the outer for loop will not be execute
	# and nothing will be done on the list itself, nothing change
	for j in range(len(list_to_sort) - 1, 0, -1):
		for i in range(j):
			if list_to_sort[i] < list_to_sort[i + 1]:
				list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
	return


def selection_sort(list_to_sort):
	"""
	The functions sorts the list in the ascending order.
	\nKey Ideas:
	\n1. Loop the number list, and determine the index of the largest number, then swap with the last number in the list
	\n2. With the largest number at the end of the number list, loop the number list again excluding the last number \
	and find the index of the largest number in the remaining list(second largest in general)
	\n3. By iterate the number list (length - 1) times, you will have the sorted list wanted
	\nTime Complexity: O(n^2) n + (n - 1) + ... + 1 = n(n + 1)/2
	\nSpace Complexity: O(1) In-place Operation

	:param list_to_sort:
	:return: None
	"""
	if not list_to_sort or len(list_to_sort) == 0:
		return None
	# The outer loop makes the number on the index i larger than any numbers before it
	for i in range(len(list_to_sort) - 1, 0, -1):
		# The inner for loop compare the number on index j with the number on max_index
		# We initialize the max index is 0 at the beginning
		max_index = 0
		for j in range(1, i + 1):
			if list_to_sort[j] > list_to_sort[max_index]:
				# if the number on this position j is greater than the number on the current max index
				max_index = j
		# Swap at the ending
		list_to_sort[max_index], list_to_sort[i] = list_to_sort[i], list_to_sort[max_index]
	return


def selection_sort_reversed(list_to_sort):
	"""
	The functions sorts the list in the descending order.

	:param list_to_sort:
	:return:
	"""
	if not list_to_sort or len(list_to_sort) == 0:
		return
	for j in range(len(list_to_sort) - 1, 0, -1):
		min_index = 0
		for i in range(1, j+1):
			if list_to_sort[i] < list_to_sort[min_index]:
				min_index = i
		list_to_sort[min_index], list_to_sort[j] = list_to_sort[j], list_to_sort[min_index]
	return


def insert_sorted(original_list, element_to_insert):
	"""
	The function inserts an element to a sorted list
	\nKey Ideas:
	\n1. Insert the element at the end of the list
	\n2. Compare the last number(element_to_insert) with the rest of the element from the end to the start and swap them
	if needed
	\nTime Complexity: O(n)
	\nSpace Complexity: O(1) In-place Operation

	:param original_list:
	:param element_to_insert:
	:return:
	"""
	# The input of the original_list has to be a list
	# even it is a empty list
	if len(original_list) == 0:
		original_list.append(element_to_insert)
		return
	# Insert the element at the end of the list
	original_list.append(element_to_insert)
	# The original list is sorted, and the new element is at the end of the list
	# We need to compare it with the numbers before it one by one, and swap them as long as the previous one is greater
	# than the current one
	for i in range(len(original_list) - 1, 0, -1):
		if original_list[i-1] > original_list[i]:
			original_list[i-1], original_list[i] = original_list[i], original_list[i-1]
	return


def insertion_sort(list_to_sort):
	"""
	The functions sorts the list in the ascending order.
	\nKey Ideas:
	\n1. Insert the element one by one into a new list
	\nTime Complexity: O(n^2) n + (n - 1) + ... + 1 = n(n + 1)/2
	\nSpace Complexity: O(n)

	:param list_to_sort:
	:return:
	"""
	new_list = []
	for i in range(len(list_to_sort)):
		insert_sorted(new_list, list_to_sort[i])
	return new_list


def insertion_sort_v1(list_to_sort):
	"""
	The functions sorts the list in the ascending order.
	\nKey Ideas:
	\n1. Start from the second number and compare with the first number, and swap if needed
	\n2. Iterate the list from front to back, keep the record of its index and value and compare it with the numbers
	after it, move every number that is smaller than it forward by one.
	\n3. Set the number to the proper position
	\nTime Complexity: O(n^2) n + (n - 1) + ... + 1 = n(n + 1)/2
	\nSpace Complexity: O(1) - The main advantage

	:param list_to_sort:
	:return:
	"""
	# It acts like insert the i-th element to the list containing the elements before it
	for i in range(1, len(list_to_sort)):
		# keep the record of the number on index i
		temp_num = list_to_sort[i]
		temp_index = i
		# when the current number is less than the number before it, set the current to be the number before it
		# and the loop cannot iterate out of the list, temp_index has to be at least one, because the loop need to access
		# the number before a certain index
		while temp_index > 0 and list_to_sort[temp_index - 1] > temp_num:
			list_to_sort[temp_index] = list_to_sort[temp_index - 1]
			temp_index -= 1
		# Right now, the temp_index is the index we need to put the temp_num in
		list_to_sort[temp_index] = temp_num


def search_and_insertion(list_to_insert, num_insert):
	"""
	The function insert an element to a sorted list
	\nKey Ideas:
	\n1. Use the search algorithm to find the closet element of the element you need to insert
	\n2. The number on the index we found could be smaller or greater than the number to insert, + 1 on index might be needed
	\n3. Insert the num at the end of the list, and move every number after the insert_position backward by 1
	\nTime Complexity: O(log2(n) + n)
	\nSpace Complexity: O(n)

	:param list_to_insert:
	:param num_insert:
	:return:
	"""
	# list_to_insert is empty at first
	if len(list_to_insert) == 0:
		list_to_insert.append(num_insert)
		return

	# Assume the list_to_insert is a sorted list
	insert_position = SearchAlgorithm.binary_search_closet_number(list_to_insert, num_insert)

	# The value of the insert position could be less or greater than the num_insert
	if list_to_insert[insert_position] < num_insert:
		insert_position += 1

	# Get the length of the original list because the insert_position is based on the previous list
	idx = len(list_to_insert)
	list_to_insert.append(num_insert)

	while idx > insert_position:
		# The number on the idx is the new inserted element
		list_to_insert[idx] = list_to_insert[idx - 1]
		idx -= 1
	list_to_insert[insert_position] = num_insert


def binary_search_help_insertion(list_to_sort):
	"""
	The functions sorts the list in the ascending order.
	\nTime Complexity: O(n * (log2(n) + n))
	\nSpace Complexity: O(n)

	:param list_to_sort:
	:return:
	"""
	new_list = []
	for i in range(len(list_to_sort)):
		print(new_list)
		search_and_insertion(new_list, list_to_sort[i])
	print(new_list)
	return new_list


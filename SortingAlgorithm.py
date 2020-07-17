"""
Updated: 2020/07/15
Author: Yunjie Wang
"""
import random

def bubble_sort(list_to_sort):
	if not list_to_sort or len(list_to_sort) == 0:
		return
	# For Special case, len = 1, the outer for loop will not be execute
	# and nothing will be done on the list itself, nothing change
	for j in range(len(list_to_sort) - 1, 0, -1):
		for i in range(j):
			if list_to_sort[i] > list_to_sort[i + 1]:
				list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
	# print(list_to_sort)
	return

def bubble_sort_reversed(list_to_sort):
	if not list_to_sort or len(list_to_sort) == 0:
		return
	# For Special case, len = 1, the outer for loop will not be execute
	# and nothing will be done on the list itself, nothing change
	for j in range(len(list_to_sort) - 1, 0, -1):
		for i in range(j):
			if list_to_sort[i] < list_to_sort[i + 1]:
				list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
	# print(list_to_sort)
	return

def selection_sort(list_to_sort):
	if not list_to_sort or len(list_to_sort) == 0:
		return
	for j in range(len(list_to_sort) - 1, 0, -1):
		max_index = 0
		for i in range(1, j+1):
			if list_to_sort[i] > list_to_sort[max_index]:
				max_index = i
		list_to_sort[max_index], list_to_sort[j] = list_to_sort[j], list_to_sort[max_index]
	# print(list_to_sort)
	return

def selection_sort_reversed(list_to_sort):
	if not list_to_sort or len(list_to_sort) == 0:
		return
	for j in range(len(list_to_sort) - 1, 0, -1):
		min_index = 0
		for i in range(1, j+1):
			if list_to_sort[i] < list_to_sort[min_index]:
				min_index = i
		list_to_sort[min_index], list_to_sort[j] = list_to_sort[j], list_to_sort[min_index]
	# print(list_to_sort)
	return

def insert_sorted(original_list, element_to_insert):
	# The input of the original_list has to be a list
	# even it is a empty list
	if len(original_list) == 0:
		original_list.append(element_to_insert)
		return
	# Insert the element at the end of the list
	original_list.append(element_to_insert)
	for i in range(len(original_list) - 1, 0, -1):
		if original_list[i-1] > original_list[i]:
			original_list[i-1], original_list[i] = original_list[i], original_list[i-1]
	return

def insertion_sort(list_to_sort):
	new_list = []
	for i in range(len(list_to_sort)):
		insert_sorted(new_list, list_to_sort[i])
	return new_list

def insertion_sort_in_place(list_to_sort):
	# For zero-or-one-element list, the for loop will not be executed
	for i in range(1, len(list_to_sort)):
		current_value = list_to_sort[i]
		k = i
		# For one-element list, the while loop will not be executed
		while k > 0 and (current_value < list_to_sort[k-1]):
			# Move the previous element to the current index(k)
			# in order to arrange a space(k-1) for the insertion
			list_to_sort[k] = list_to_sort[k-1]
			k -= 1
		# The while loop is out, the proper position is found
		list_to_sort[k] = current_value


a = [random.randrange(0,2000) for i in range(500)]
print(a)
insertion_sort_in_place(a)
print(a)
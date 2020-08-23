"""
Updated: 2020/08/22
Author: Yunjie Wang
"""
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import random
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


class BinarySearch(object):
	"""
	The class provides several functions based on the idea of the binary search.
	In the initialization, users need to provide a SORTED list and a target.
	Every function under this class is based on the assumption of the sorted list input also a valid target input
	"""
	def __init__(self, sorted_list, target):
		self.sorted_list = sorted_list
		self.target = target
		# At the beginning of the certain function, it will be set to "NOT FOUND"
		# The result will be a number string if the actual function returns the position index
		# If the function fails to find the target, it will remain "NOT FOUND"
		self.result = None
		# The oper variable represent the actual function in use
		self.oper = None

	def classic_binary_search(self):
		"""
		The function calls the inner function performing classic binary research
		And it will set the result(string) based on the return of the inner function

		:return: None
		"""
		self.result = "NOT FOUND"
		res = self._classic_binary_search()
		if res != -1:
			self.result = str(res)

	def _classic_binary_search(self):
		"""
		The function performs binary searching on the input list for the target
		\nGoal: Find a number in a sorted list
		\nKey Observation:

		:return: position index if the target is found, -1 otherwise
		"""













def plot_pause_erase(fig_obj):
	fig_obj.show()
	plt.pause(2)
	plt.clf()

def set_xylimit(axis_plot, list_length, list_max, list_min, ratio=1.1):

	# This will depend on the size and the value of the list
	# The ratio will extend the limit a bit for the plotting reason, set it to 1 for now
	axis_plot.xaxis.set_major_locator(MaxNLocator(integer=True))
	axis_plot.yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.xlim([-1, list_length])
	upper_bound = list_max * ratio if list_max > 0 else list_max / ratio
	lower_bound = list_min / ratio if list_min > 0 else list_min * ratio
	upper_bound = math.ceil(upper_bound)
	lower_bound = math.floor(lower_bound)
	# print(upper_bound, lower_bound)
	plt.ylim([lower_bound, upper_bound])

def erase_one_point_from_list(list_to_erase, index):
	list_to_erase[index] = 0

def prepare_one_point_plot(list_to_prepare, list_to_copy, index):
	list_to_prepare[index] = list_to_copy[index]

def erase_lr_on_baselist(left_index, right_index, base_list):
	erase_one_point_from_list(base_list, left_index)
	erase_one_point_from_list(base_list, right_index)

def prepare_lr_plotlist(left_index, right_index, lr_list, orginal_list):
	prepare_one_point_plot(lr_list, orginal_list, left_index)
	prepare_one_point_plot(lr_list, orginal_list, right_index)

def binarySearch(numList, target):
	# For plot purpose
	list_length = len(numList)
	list_max = max(numList)
	list_min = min(numList)
	# Create a copy of it because I don't want to mess up the original list
	base_list_plot = numList[:]

	# If the number list is empty, return None representing (NOT FOUND)
	if not numList:
		return None

	plt.title("Binary searching for {0}".format(target))
	fig = plt.gcf()
	ax = plt.gca()

	set_xylimit(ax, list_length, list_max, list_min)

	# Create new empty lists to store the L,R,Mid
	left_right_plot = [0] * len(numList)
	# This x_axis represents the index of the list
	x_axis_plot = [i for i in range(len(numList))]
	# The last number in the color is the transparency
	plt.bar(x_axis_plot, base_list_plot, color=(1, 0, 0, 1))
	plt.xlabel("Index")
	plot_pause_erase(fig)
	# At first, set the left and right to the start and end index of the number list
	left = 0
	right = len(numList) - 1
	# return
	# Since we don't know how many times we need to run the loop, choose while loop
	# The ending case will be only one number and that one is not the number we want
	while left <= right:
		mid = (left+right) // 2
		plt.title("L:{0}@{4}, R:{1}@{5}, Mid:{2}@{6}, Target:{3}".format(numList[left], numList[right], numList[mid], target,
		                                                                 left, right, mid))
		ax = plt.gca()
		# Create a copy of it because I don't want to mess up the original list
		base_list_plot = numList[:]
		# Refresh it to all-0 again
		# Create a new empty list to store the L,R,Mid
		left_right_plot = [0] * list_length
		mid_plot = [0] * list_length

		# Successfully found and return the index of it
		if numList[mid] == target:
			erase_one_point_from_list(base_list_plot, mid)
			prepare_one_point_plot(mid_plot, numList, mid)
			plt.title("FOUND IT! {0}@{1}".format(target, mid))
			set_xylimit(ax, list_length, list_max, list_min)
			plt.bar(x_axis_plot, base_list_plot, color=(1, 0, 0, 1))
			plt.bar(x_axis_plot, mid_plot, color=(0, 0, 1, 1))
			for index, value in enumerate(mid_plot):
				if index == mid:
					# The position need to be fixed!!!
					# plt.annotate(value, xy=(index, value), xytext=(index, value*1.1),arrowprops=dict(facecolor='black', shrink=0.05))
					plt.text(index, value ,r"$\bf" + '{}'.format(value) + "$", horizontalalignment='center')
			plot_pause_erase(fig)

			return mid
		# The target is at the right side of the midpoint, we need to push the left to the (midpoint+1)
		elif numList[mid] < target:
			# Plot
			erase_lr_on_baselist(left, right, base_list_plot)
			prepare_lr_plotlist(left, right, left_right_plot, numList)
			set_xylimit(ax, list_length, list_max, list_min)
			plt.bar(x_axis_plot, base_list_plot, color=(1, 0, 0, 1))
			plt.bar(x_axis_plot, left_right_plot, color=(0, 1, 0, 1))
			# plt.bar(x_axis_plot, mid_plot, color=(0, 0, 1, 1))
			plot_pause_erase(fig)

			left = mid + 1 # The midpoint is for sure not the target, so we can start the "new" list from the next one

		# The target is at the left side of the midpoint, we need to push the right to the (midpoint+1)
		elif numList[mid] > target:
			# Plot
			erase_lr_on_baselist(left, right, base_list_plot)
			prepare_lr_plotlist(left, right, left_right_plot, numList)
			set_xylimit(ax, list_length, list_max, list_min)
			plt.bar(x_axis_plot, base_list_plot, color=(1, 0, 0, 1))
			plt.bar(x_axis_plot, left_right_plot, color=(0, 1, 0, 1))
			# plt.bar(x_axis_plot, mid_plot, color=(0, 0, 1, 1))
			plot_pause_erase(fig)

			right = mid - 1

	# Even the one last number is not the number we want, the target must not be in the number list
	plt.title("{0} NOT FOUND".format(target))
	if left not in range(list_length):
		left = (list_length - 1)
	if right not in range(list_length):
		right = 0
	erase_lr_on_baselist(left, right, base_list_plot)
	prepare_lr_plotlist(left, right, left_right_plot, numList)
	set_xylimit(ax, list_length, list_max, list_min)
	plt.bar(x_axis_plot, base_list_plot, color=(1, 0, 0, 1))
	plt.bar(x_axis_plot, left_right_plot, color=(0, 1, 0, 1))
	for index, value in enumerate(left_right_plot):
		if index in [left, right]:
			plt.text(index, value, r"$\bf" + '{}'.format(value) + "$", horizontalalignment='center')
	plot_pause_erase(fig)
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

def my_custom_random():
	exclude=[0]
	randInt = random.randrange(-100,100)
	return my_custom_random() if randInt in exclude else randInt

def merge_two_lists(list1, list2):
	"""
	:param list1,2 : Sorted lists
	:return: A sorted list
	"""
	new_list = []
	i = 0
	j = 0
	while i < len(list1) and j < len(list2):
		if list1[i] < list2[j]:
			new_list.append(list1[i])
			i += 1
		else:
			new_list.append(list2[j])
			j += 1
	# The length of two lists might not be the same
	# At most one line from the following two will have actual effect on the new_list
	while i < len(list1):
		new_list.append(list1[i])
		i += 1
	while j < len(list2):
		new_list.append(list2[j])
		j += 1
	return new_list

def merge_sort(list_to_sort):
	if len(list_to_sort) == 0 or len(list_to_sort) == 1:
		return list_to_sort
	mid = (len(list_to_sort) + 1) // 2
	left = merge_sort(list_to_sort[:mid])
	right = merge_sort(list_to_sort[mid:])
	return merge_two_lists(left, right)

def partition(alist, start, end, pivot_index):
	# In this list, every element before the pivot_index is less than the number on it,
	# every element after the pivot_index is greater than the number on it.

	# Swap the number on the pivot index and the last number of the list
	alist[pivot_index] , alist[end] = alist[end] , alist[pivot_index]
	small_index = start
	for i in range(start, end):
		if alist[i] < alist[end]:
			alist[i], alist[small_index] = alist[small_index], alist[i]
			small_index += 1
	alist[small_index], alist[end] = alist[end], alist[small_index]
	return small_index

def quick_sort_helper(alist, start, end):
	if start >= end:
		return
	random_num = random.randrange(start, end + 1)
	pivot_index = partition(alist, start, end, random_num)
	quick_sort_helper(alist, start, pivot_index - 1)
	quick_sort_helper(alist, pivot_index + 1, end)

def quick_sort(list_to_sort):
	quick_sort_helper(list_to_sort, 0, len(list_to_sort) - 1)

# a = [28, 1, -1 ,5]
# quick_sort(a)
# print(a)

# # Test
# for j in range(100):
# 	testList = sorted(my_custom_random() for i in range(100))
# 	# print(testList)
# 	print(binarySearch(testList, random.randrange(-200, 200)))
# alist = [2,1,0,3,-1,5,1,5,6,8,9,1,7]
# new_list = merge_sort(alist)
# print(new_list)
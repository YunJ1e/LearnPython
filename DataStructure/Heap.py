"""
Updated: 2020/08/11
Author: Yunjie Wang
"""


# Min heap and Max heap
# max heap: every node is greater than its child
# min heap: every node is less than its child

# We can use list in the Python to implement our heap structure

# left_child_node_index = parent_node_index * 2 + 1
# right_child_node_index = parent_node_index * 2 + 2
# parent_node_index = (child_node_index - 1) // 2
# What if we find that the parent node index is negative? The current node is the root.

# min heap


class Heap(object):
	def __init__(self, array):
		"""
		We use the list to implement the heap structure with the relationship between indices
		"""
		self.array = self.build_heap(array)
		# self.array.

	def sift_up_recursion(self, array, index):
		"""
		Given an index, arrange the number on that index to the correct position
		:param index: The input index
		:param array: The input array
		:return: None
		"""
		# Its parent index
		parent_index = (index - 1) // 2
		# If the parent index is less than 0, it means the original index is the root index
		# These are two ending cases:
		#   1. The number on "index" ends up on the top of the heap
		#   2. The number on "index" swapping ending in the middle
		if parent_index < 0 or array[parent_index] < array[index]:
			return
		array[parent_index], array[index] = array[index], array[parent_index]
		self.sift_up_recursion(parent_index, array)

	def sift_up_iteration(self, array, index):
		"""
		Given an index, arrange the number on that index to the correct position
		:param index: The input index
		:param array: The input array
		:return: None
		"""
		# Its parent index
		parent_index = (index - 1) // 2
		# If the parent index is less than 0, it means the original index is the root index
		# These are two ending cases:
		#   1. The number on "index" ends up on the top of the heap
		#   2. The number on "index" swapping ending in the middle
		# The first case will end the while loop for sure
		while parent_index >= 0:
			# For the second cases
			if array[parent_index] < array[index]:
				return
			array[parent_index], array[index] = array[index], array[parent_index]
			index = parent_index
			parent_index = (index - 1) // 2

	def push(self, val):
		"""
		This function will take the advantage of the sift up to realize the push operation
		:param val: The number I want to push into the heap
		:return: None
		"""
		self.array.append(val)
		self.sift_up_recursion(self.array, len(self.array) - 1)

	def sift_down_recursion(self, array, index):
		"""
		This function is to re-arrange the list to be a heap
		:param index: usually 0
		:param array: the input array
		:return: None
		"""
		left_child_index = 2 * index + 1
		right_child_index = 2 * index + 2
		smaller = index

		if left_child_index < len(array) and array[left_child_index] < array[smaller]:
			smaller = left_child_index
		if right_child_index < len(array) and array[right_child_index] < array[smaller]:
			smaller = right_child_index

		if smaller != index:
			# There are swaps happening
			array[smaller], array[index] = array[index], array[smaller]
			self.sift_down_recursion(array, smaller)

	def sift_down_iteration(self, array, index):
		"""
		This function is to re-arrange the list to be a heap
		:param index: usually 0
		:param array: the input array
		:return: None
		"""
		left_child_index = 2 * index + 1
		right_child_index = 2 * index + 2

		while left_child_index < len(array):
			smaller = index
			if left_child_index < len(array) and array[left_child_index] < array[smaller]:
				smaller = left_child_index
			if right_child_index < len(array) and array[right_child_index] < array[smaller]:
				smaller = right_child_index
			if smaller == index:
				# There is no swap anymore
				break
			# There are swaps happening
			array[smaller], array[index] = array[index], array[smaller]
			index = smaller
			left_child_index = 2 * smaller + 1
			right_child_index = 2 * smaller + 2

	def pop(self):
		"""
		The function will return the min from the heap and keeping the heap structure at the same time
		:return: min of the heap
		"""
		ret_value = self.array[0]
		# Swap the first and the last of the heap for the sake of the simplicity
		self.array[0], self.array[-1] = self.array[-1], self.array[0]
		self.array.pop()
		self.sift_down_recursion(self.array, 0)
		return ret_value

	def build_heap(self, array):
		"""
		This function will take in an array and return a heap that includes all number in the original array
		:param array: the input array
		:return: a heap array
		"""
		# All leaf in the complete binary tree
		for i in range(len(array) // 2 - 1, -1, -1):
			self.sift_down_recursion(array, i)
		return array



"""
Updated: 2020/08/14
Author: Yunjie Wang
"""
# There is a library in Python which can help us with the heap-related structure
import heapq

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


class KSmallest(object):
	"""
	The object solves the K smallest problem and several problems which are similar with it
	"""
	def __init__(self):
		self._unsorted_list = None
		self._k_num = None
		self._operation = "No Operation"
		self._result = None

	def set_list(self, input_list):
		"""
		The function sets the input list
		:param input_list: An unsorted list
		:return: None
		"""
		self._unsorted_list = input_list

	def get_list(self):
		"""
		The function returns the input list
		:return: The input list
		"""
		return self._unsorted_list

	def set_k(self, input_k):
		"""
		The function sets the K number
		:param input_k: The K
		:return: None
		"""
		self._k_num = input_k

	def get_k(self):
		"""
		The function returns the K number
		:return: The K
		"""
		return self._k_num

	def _set_result(self, input_result):
		"""
		The function sets the result after operation
		:param input_result: The result
		:return: None
		"""
		self._result = input_result

	def get_result(self):
		"""
		The function returns the result
		:return: The result
		"""
		return self._result

	def _smallest_k_elements(self):
		"""
		The function finds smallest K elements from an unsorted list
			1. Heapify the unsorted list
			2. Pop the heap k times(needed comparison with the length of list) and append the element into the res
		:return: None
		"""
		if not self._unsorted_list or not self._k_num:
			self._result = None
			return
		self._operation = "Find Smallest {0} Elements".format(self.get_k())
		res = []
		list_copy = self._unsorted_list[:]
		heapq.heapify(list_copy)
		for i in range(min(len(list_copy), self._k_num)):
			res.append(heapq.heappop(list_copy))
		self._set_result(res)

	def _smallest_k_elements_v2(self):
		"""
		The function finds smallest K elements from an unsorted list
			1. Heapify the first k element from the unsorted list
				1.1 We may need the max heap for this problem
				1.2 To achieve the max heap, we could add extra "-" for the number list
					And the top of the heap is the largest number from first K elements with a extra "-" in front of it

			2. Continually comparing the following number, if the negative of it is smaller than the top of the heap,
			which actually means that the number is larger than the largest from the first K number, we will ignore it
			because it is for sure not in the list of target

		:return: None
		"""
		if not self._unsorted_list or not self._k_num:
			self._result = None
			return
		self._operation = "Find Smallest {0} Elements".format(self.get_k())
		res = [-element for element in self._unsorted_list[0:self._k_num]]
		heapq.heapify(res)
		for i in range(self._k_num, len(self._unsorted_list)):
			if self._unsorted_list[i] < -res[0]:
				heapq.heappop(res)
				heapq.heappush(res, -self._unsorted_list[i])
		self._set_result([-element for element in res])

	def smallest_k_elements(self):
		"""
		The function finds smallest K elements from an unsorted list
		:return: None
		"""
		self._smallest_k_elements_v2()

	def _smallest_kth_element(self):
		"""
		The function finds smallest Kth elements from an unsorted list
			By using the function of finding k-th smallest numbers. and return the last number of the origin result
		:return: None
		"""
		if not self._unsorted_list or not self._k_num:
			self._result = None
			return
		self._smallest_k_elements()
		self._operation = "Find Smallest {0}-th Elements".format(self.get_k())
		self._set_result(self.get_result()[-1])

	def smallest_kth_element(self):
		"""
		The function finds smallest Kth elements from an unsorted list
		:return: None
		"""
		self._smallest_kth_element()

	def _largest_k_elements(self):
		"""
		The function finds the largest K number
		:return: None
		"""
		if not self._unsorted_list or not self._k_num:
			self._result = None
			return
		self._operation = "Find Largest {0} Elements".format(self.get_k())
		res = [element for element in self._unsorted_list[0:self._k_num]]
		heapq.heapify(res)
		for i in range(self._k_num, len(self._unsorted_list)):
			if self._unsorted_list[i] > res[0]:
				heapq.heappop(res)
				heapq.heappush(res, self._unsorted_list[i])
		self._set_result([element for element in res])

	def largest_k_elements(self):
		"""
		The function finds the largest K number
		:return: None
		"""
		self._largest_k_elements()

	def _largest_kth_element(self):
		"""
		The function finds largest Kth elements from an unsorted list
			By using the function of finding k-th largest numbers. and return the fist number of the origin result
		:return: None
		"""
		if not self._unsorted_list or not self._k_num:
			self._result = None
			return
		self._largest_k_elements()
		self._operation = "Find Largest {0}-th Elements".format(self.get_k())
		self._set_result(self.get_result()[0])

	def largest_kth_element(self):
		"""
		The function finds largest Kth elements from an unsorted list
		:return: None
		"""
		self._largest_kth_element()

	def __str__(self):
		res = self._operation
		res += "\n- Input: {0}\n- Output: {1}\n".format(self.get_list(), self.get_result())
		res += "-" * 20
		return res

# Test
# a = KSmallest()
# a.set_k(3)
# a.set_list([5, 4, 3, 2, 1, 0, -1, 20, 10])
# a.smallest_k_elements()
# print(a)
# a.smallest_kth_element()
# print(a)
# a.largest_k_elements()
# print(a)
# a.largest_kth_element()
# print(a)


class MergeKSorted():
	"""
	The object solves merge K lists problem
	"""
	def __init__(self):
		self._sorted_list = None
		self._operation = "No Operation\n"
		self._result = None

	def set_list(self, input_list):
		"""
		The function sets the input list
		:param input_list: An list of sorted lists
		:return: None
		"""
		self._sorted_list = input_list

	def get_list(self):
		"""
		The function returns the input list
		:return: The input list
		"""
		return self._sorted_list

	def _set_result(self, input_result):
		"""
		The function sets the result after operation
		:param input_result: The result
		:return: None
		"""
		self._result = input_result

	def get_result(self):
		"""
		The function returns the result
		:return: The result
		"""
		return self._result

	def _merge(self):
		"""
		The functions merge the K sorted lists into one sorted list
		:return: The merged list
		"""
		if not self._sorted_list:
			return None
		self._operation = "Merge {0} Sorted Lists\n".format(len(self._sorted_list))
		aList = []
		for i in range(len(self._sorted_list)):
			if len(self._sorted_list[i]):
				aList.append((self._sorted_list[i][0], i, 0))
		heapq.heapify(aList)
		res = []
		while aList:
			val, array_index, element_index = heapq.heappop(aList)
			res.append(val)
			if element_index + 1 < len(self._sorted_list[array_index]):
				heapq.heappush(aList, (self._sorted_list[array_index][element_index + 1], array_index, element_index + 1))
		return res

	def merge(self):
		"""
		The function sets the result returned from inner function to the result attribute
		:return: None
		"""
		self._set_result(self._merge())

	def _smallest_range(self):
		"""
		The functions returns the smallest range of three numbers picked from K sorted list
		:return: A list containing lower and upper bound of the range
		"""
		if not self._sorted_list:
			return None
		self._operation = "Find the Smallest Range with {0} numbers\n".format(len(self._sorted_list))
		aList = []
		max_value = -float("inf")
		for i in range(len(self._sorted_list)):
			if len(self._sorted_list[i]):
				aList.append((self._sorted_list[i][0], i, 0))
				max_value = max(max_value, self._sorted_list[i][0])
		heapq.heapify(aList)
		res = [-float("inf"), float("inf")]
		while len(aList) == len(self._sorted_list):
			val, array_index, element_index = heapq.heappop(aList)
			if max_value - val < res[1] - res[0]:
				res = [val, max_value]
			if element_index + 1 < len(self._sorted_list[array_index]):
				heapq.heappush(aList, (self._sorted_list[array_index][element_index + 1], array_index, element_index + 1))
				max_value = max(max_value, self._sorted_list[array_index][element_index + 1])
		return res

	def smaller_range(self):
		"""
		The functions sets the result of the range found
		:return: None
		"""
		self._set_result(self._smallest_range())

	def __str__(self):
		res = self._operation
		res += "- Input: "
		for i in range(len(self.get_list())):
			res += str(self.get_list()[i])
			if i == len(self.get_list()) - 1:
				res += "\n"
			else:
				res += ", "
		res += "- Output: "
		res += str(self.get_result())

		return res


# Test
b = MergeKSorted()
b.set_list([
	[1, 4, 6],
	[2, 5],
	[8, 10, 15]])
b.merge()
print(b)

b.smaller_range()
print(b)

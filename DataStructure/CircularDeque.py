# First of all, I try to implement based on list, because it is relatively easier with the help of certain features
# But the adding and removing from head function will COST O(n), which is not ideal
class circular_deque(object):
	# Do not use the built-in deque function
	def __init__(self, k):
		"""
		Initialize your data structure here. Set the size of the deque to be k.
		"""
		self._items = []
		self._size = k

	def __len__(self):
		return len(self._items)

	def insertFront(self, value):
		"""
		Adds an item at the front of Deque. Return true if the operation is successful.
		"""
		if not self._items:
			self._items = [value]
		elif self.isFull():
			return False
		else:
			self._items.insert(0, value)
		return True

	def insertLast(self, value):
		"""
		Adds an item at the rear of Deque. Return true if the operation is successful.
		:type value: int
		:rtype: bool
		"""
		if not self._items:
			self._items = [value]
		elif self.isFull():
			return False
		else:
			self._items.append(value)
		return True

	def deleteFront(self):
		"""
		Deletes an item from the front of Deque. Return true if the operation is successful.
		:rtype: bool
		"""
		if self.isEmpty():
			return False
		else:
			self._items.pop(0)
		return True

	def deleteLast(self):
		"""
		Deletes an item from the rear of Deque. Return true if the operation is successful.
		:rtype: bool
		"""
		if self.isEmpty():
			return False
		else:
			self._items.pop(-1)
		return True

	def getFront(self):
		"""
		Get the front item from the deque.
		:rtype: int
		"""
		if not self.isEmpty():
			return self._items[0]

	def getRear(self):
		"""
		Get the last item from the deque.
		:rtype: int
		"""
		if not self.isEmpty():
			return self._items[-1]

	def isEmpty(self):
		"""
		Checks whether the circular deque is empty or not.
		:rtype: bool
		"""
		return self.__len__() == 0

	def isFull(self):
		"""
		Checks whether the circular deque is full or not.
		:rtype: bool
		"""
		return self.__len__() == self._size

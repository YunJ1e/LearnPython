class circular_queue(object):
	# Do not use the built-in deque function
	def __init__(self, k):
		"""
		Initialize your data structure here. Set the size of the queue to be k.
		:type k: int
		"""
		self._items = []
		self._size = k

	def __len__(self):
		return len(self._items)

	def enQueue(self, value):
		"""
		Insert an element into the circular queue. Return true if the operation is successful.
		:type value: int
		:rtype: bool
		"""
		if self.isFull():
			return False
		elif self.isEmpty():
			self._items = [value]
		else:
			self._items.append(value)
		return True

	def deQueue(self):
		"""
		Delete an element from the circular queue. Return true if the operation is successful.
		:rtype: bool
		"""
		if self.isEmpty():
			return False
		else:
			self._items.pop(0)
		return True

	def Front(self):
		"""
		Get the front item from the queue.
		:rtype: int
		"""
		if not self.isEmpty():
			return self._items[0]

	def Rear(self):
		"""
		Get the last item from the queue.
		:rtype: int
		"""
		if not self.isEmpty():
			return self._items[-1]

	def isEmpty(self):
		"""
		Checks whether the circular queue is empty or not.
		:rtype: bool
		"""
		return self.__len__() == 0

	def isFull(self):
		"""
		Checks whether the circular queue is full or not.
		:rtype: bool
		"""
		return self.__len__() == self._size

"""
Updated: 2020/07/18
Author: Yunjie Wang
"""
import random
"""
LinkedList - OOP
"""


class _ListNode(object):
	# Since the node is the basic unit of the linked list,
	# _ symbol means that I do not recommend the user directly touch it
	def __init__(self,val):
		self.next = None
		self.value = val


class LinkedList(object):
	def __init__(self):
		# For a linked list, there are some fundamental attributes we cannot skip
		# We do not want the user to mess up the head and tail information
		self._head = None
		self._tail = None
		self._size = 0

	def random_generate(self, llist_size):
		for i in range(llist_size):
			self.add_at_index(i, random.randrange(0,20))

	def generate_based_on_list(self, list_to_insert):
		for num in list_to_insert:
			self.add_at_tail(num)

	def _get(self, index):
		# get the node, this is not the function user can interact with
		curr = self._head
		for i in range(index):
			curr = curr.next
		return curr

	def get(self, index):
		# get the value on the node
		if index < 0 or index >= self._size:
			return None
		return self._get(index).value

	def add_at_head(self, value):
		if self._size == 0:
			self._head = self._tail = _ListNode(value)
		else:
			new_node = _ListNode(value)
			new_node.next = self._head
			self._head = new_node

		self._size += 1

	def add_at_tail(self, value):
		if self._size == 0:
			self._head = self._tail = _ListNode(value)
		else:
			new_node = _ListNode(value)
			self._tail.next = new_node
			self._tail = self._tail.next

		self._size += 1

	def add_at_index(self, index, value):
		if index < 0 or index > self._size:
			return
		if index == 0:
			self.add_at_head(value)
		elif index == self._size:
			self.add_at_tail(value)
		else:
			prev_node = self._get(index - 1)
			new_node = _ListNode(value)
			new_node.next = prev_node.next
			prev_node.next = new_node
			self._size += 1

	def delete_at_head(self):
		newHead = self._head.next
		self._head.next = None
		self._head = newHead
		# No node in the linked list
		if self._head is None:
			self._tail = None

	def delete_at_index(self, index):
		if index < 0 or index >= self._size:
			return
		if index == 0:
			self.delete_at_head()
		else:
			pre_node_to_delete = self._get(index - 1)
			node_to_delete = pre_node_to_delete.next
			pre_node_to_delete.next = node_to_delete.next
			node_to_delete.next = None
			if index == self._size - 1:
				self._tail = pre_node_to_delete

	def __str__(self):
		node_val_list = []
		curr = self._head
		while curr is not None:
			node_val_list.append(str(curr.value))
			curr = curr.next
		return " -> ".join(node_val_list)

# myLList = LinkedList()
# myLList.random_generate(10)
# myLList.generate_based_on_list([1, 2, 3, 4, 5])
# myLList.add_at_index(3,8)
# myLList.delete_at_index(7)
# print(myLList)
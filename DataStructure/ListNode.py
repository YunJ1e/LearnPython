"""
Updated: 2020/07/18
Author: Yunjie Wang
"""

import random
"""
ListNode - OOP
This file contains a new data structure and several free functions that operate
on this kind of structure
"""


class ListNode(object):
	# The basic unit of the linked-list
	def __init__(self, val):
		self.next = None
		self.value = val

	def __eq__(self, other):
		return isinstance(other, ListNode) and (other.value == self.value)

	def __str__(self):
		return "Node value: {}".format(self.value)

def reverse_llist(head):
	if not head:
		return None
	current = head
	pre = None

	while current.next is not None:
		next_node = current.next
		current.next = pre
		pre = current
		current = next_node
	current.next = pre
	return current

def llist_random_generator(list_length):
	if list_length <= 0:
		return

	fake_head = ListNode(-1)
	curr = fake_head
	for i in range(list_length):
		curr.next = ListNode(random.randrange(0, 20))
		curr = curr.next
		print(curr.value)
	return fake_head.next

def llist_based_on_list(list_to_covert):
	if len(list_to_covert) == 0:
		return None

	fake_head = ListNode(-1)
	curr = fake_head
	for num in list_to_covert:
		curr.next = ListNode(num)
		curr = curr.next
	return fake_head.next

def traverse(node_to_print):
	while node_to_print is not None:
		print(node_to_print.value, end=" -> ")
		node_to_print = node_to_print.next
	print("None")

def search_by_index(headNode, index_to_find):
	"""
	:param: A singly linked list and an index(assume the index of the first node is 0)
	:return: Returns the node I found, otherwise return None
	"""
	if headNode is None or index_to_find < 0:
		return None

	for i in range(index_to_find):
		if headNode.next is None:
			# The linked list is out of index
			return None
		headNode = headNode.next

	return headNode

def search_by_value(headNode, target):
	"""
	:param headNode: A singly linked list and an index(assume the index of the first node is 0)
	:param target: A number to find
	:return: A node if found, otherwise None
	"""
	if headNode is None:
		return None
	current_node = headNode
	while current_node is not None:
		if current_node.value == target:
			return current_node
		current_node = current_node.next
	return None

def add_to_index(headNode, index_to_add, value):
	"""
	:param headNode:
	:param index_to_add:
	:param value:
	:return: A singly linked list after the insertion
	"""
	fake_head = ListNode(-1)
	fake_head.next = headNode
	# With the help of the fake head and search_by_index function,
	# we can have the node before the index we want to insert
	insertion_pos = search_by_index(fake_head, index_to_add)
	# In case we do not find the proper index
	if insertion_pos is None:
		return fake_head.next
	new_node = ListNode(value)
	new_node.next = insertion_pos.next
	insertion_pos.next = new_node
	return fake_head.next

def add_to_index_v1(headNode, index_to_add, value):
	"""
	:param headNode:
	:param index_to_add:
	:param value:
	:return:
	"""
	if headNode is None or index_to_add < 0:
		return headNode
	if index_to_add == 0:
		# Special Case
		new_node = ListNode(value)
		new_node.next = headNode
		return new_node
	else:
		pre_node = search_by_index(headNode, index_to_add - 1)
		if pre_node is None:
			return headNode
		new_node = ListNode(value)
		new_node.next = pre_node.next
		pre_node.next = new_node
		return headNode

def remove_from_index(headNode, index_to_remove):
	"""
	:param headNode:
	:param index_to_remove:
	:return:
	"""
	fake_head = ListNode(-1)
	fake_head.next = headNode
	pre_remove_pos = search_by_index(fake_head, index_to_remove)
	if pre_remove_pos is None or pre_remove_pos.next is None:
		return fake_head.next
	remove_pos = pre_remove_pos.next
	pre_remove_pos.next = remove_pos.next
	remove_pos.next = None
	return fake_head.next

a = llist_random_generator()
traverse(a)
b = reverse_llist(a)
traverse(b)
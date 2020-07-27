"""
Updated: 2020/07/24
Author: Yunjie Wang
"""

"""
Queue
There are two ways implementing this data structure and one built-in feature in the Python(deque)
I prefer the linked-list version because it has certain advantages on the complexity.
	The dequeue process in the list version will have O(n) on time complexity, because it has to move every element
	forward by one index
Also there are a few problems which are better to be solved with the queue structure, and I will put it at the end.
"""
from DataStructure.LinkedList import _ListNode
from collections import deque
import operator
# This first one is using list
# class Queue(object):
# 	def __init__(self):
# 		# Initialize a empty list representing the queue
# 		self._items = []
# 	def __len__(self):
# 		# returns the number of items
# 		return len(self._items)
# 	def enqueue(self, element):
# 		# puts the item into the queue
# 		self._items.append(element)
# 	def dequeue(self):
# 		# take out the item that has been in the list for the longest time
# 		if self.is_empty():
# 			return
# 		else:
# 			item_pop = self._items.pop(0)
# 		return item_pop
# 	def is_empty(self):
# 		# return True if the list is empty
# 		return len(self._items) == 0
# 	def front(self):
# 		# return the item in the list for the longest time and without removing it
# 		if self.is_empty():
# 			return
# 		else:
# 			return self._items[0]

# This second one is using linked-list, which has only O(1) complexity for the dequeue this time

class Queue(object):
	# It is actually a simplified version of the linked list
	def __init__(self):
		# Initialize a empty list representing the queue
		self._size = 0
		self._head = None
		self._tail = None

	def __len__(self):
		# returns the number of items
		return self._size

	def enqueue(self, element):
		# puts the item into the queue
		if self._size == 0:
			self._head = self._tail = _ListNode(element)
		else:
			old_tail = self._tail
			old_tail.next = _ListNode(element)
			self._tail = old_tail.next
		self._size += 1

	def dequeue(self):
		# take out the item that has been in the list for the longest time
		if self.is_empty():
			return None
		old_head = self._head
		old_head_value = old_head.value
		self._head = old_head.next
		old_head.next = None
		if self.is_empty():
			self._tail = None
		self._size -= 1
		return old_head_value

	def is_empty(self):
		# return True if the list is empty
		return self._size == 0

	def front(self):
		# return the item in the list for the longest time and without removing it
		if self.is_empty():
			return None
		return self._head.value

# Python built-in deque(double ended queue)
def deque_test():
	# Declaration
	d = deque()
	print(d)
	# Append
	d.append(1)
	d.appendleft(2)
	print(d)

def check_valid_queue_sequence(pushed_queue, popped_queue):
	new_popped_queue = deque()
	j = 0
	for i in pushed_queue:
		new_popped_queue.append(i)

		while len(new_popped_queue) > 0 and j < len(popped_queue) and new_popped_queue[0] == popped_queue[j]:
			new_popped_queue.popleft()
			j += 1
	return j == len(popped_queue)

# a = deque([0,1,2,3,4,5])
# b = deque([0,1,2,3,4,5])
# print(check_valid_queue_sequence(a, b))

class moving_average(object):
	def __init__(self, value):
		self._window = deque()
		self._size = value
		self._sum = 0

	def __len__(self):
		return len(self._window)

	def next(self,value):
		self._window.append(value)
		self._sum += value

		if self.__len__() > self._size:
			num_to_pop = self._window.popleft()
			self._sum -= num_to_pop

		return self._sum / len(self._window)

	def __str__(self):
		alist = []
		for i in range(len(self._window)):
			alist.append(str(self._window[i]))
		return ", ".join(alist)

# a = moving_average(5)
# for i in range(10):
# 	a.next(i)
# 	print(a)

class stack(object):
	# In the case of the stack, we can see that for these simple operations, the time complexity are all O(1)
	def __init__(self):
		# initialize a empty stack
		self._items = []

	def __len__(self):
		# return the number of elements in the stack
		return len(self._items)

	def is_empty(self):
		# return True if the stack is empty
		return 0 == self.__len__()

	def push(self, value):
		# put the number into the stack
		self._items.append(value)

	def pop(self):
		# remove the number on the top of the stack and return it
		if self.is_empty():
			return None
		return self._items.pop()

	def top(self):
		# return the element on the top of the stack
		if self.is_empty():
			return None
		return self._items[-1]

def check_valid_stack_sequence(pushed_queue, popped_queue):
	new_popped_stack = deque()
	j = 0
	for i in pushed_queue:
		new_popped_stack.append(i)
		while len(new_popped_stack) > 0 and new_popped_stack[-1] == popped_queue[j] and j < len(popped_queue):
			new_popped_stack.pop()
			j += 1
	return j == len(popped_queue)

# a = deque([0,1,2,3,4,5,6,7,8,9])
# b = deque([1,2,3,4,5,6,9,8,7,0])
# print(check_valid_stack_sequence(a, b))

def is_balanced_parentheses(aString):
	# If the input is None or the string input has length 0
	if not aString or len(aString) == 0:
		return None
	# If the length cannot be divided by 2, the string is not balanced for sure
	if len(aString) % 2 != 0:
		return False
	symbol = {"(": ")", "{":"}", "[":"]"}
	aDeque = deque()
	for letter in aString:
		if letter in symbol.keys():
			aDeque.append(letter)
		elif len(aDeque) > 0 and symbol[aDeque[-1]] == letter:
			aDeque.pop()
		else:
			return False
	return len(aDeque) == 0

# print(is_balanced_parentheses("{[{}]{}[()]]"))

def arithmetic_expression_eval(terms):
	# The expression right now only contains the + - * / and non-negative numbers
	operands = deque()  # stack-like
	operators = deque()  # stack-like
	operator_target = ["+", "-", "*", "/"]
	operations = {
		"+": operator.add,
		"-": operator.sub,
		"*":operator.mul,
		"/":operator.truediv
	}
	for letter in terms:
		if letter == "(":
			continue
		elif letter == ")":
			# do the calculation
			oper = operators.pop()
			right, left = operands.pop(), operands.pop()
			res = operations[oper](left, right)
			operands.append(res)
		elif letter in operator_target:
			operators.append(letter)
		else:
			operands.append(int(letter))
	return operands.pop()

print(arithmetic_expression_eval("(1+(2/3))"))
"""
Updated: 2020/08/07
Author: Yunjie Wang
"""
class _TreeNode(object):
	def __init__(self, x):
		self.value = x
		self.left = None
		self.right = None
		self.left_total = 0
		self.right_total = 0

def random_tree():
	root = _TreeNode(1)
	root.left = _TreeNode(3)
	root.right = _TreeNode(4)
	root.left.left = _TreeNode(5)
	root.left.right = _TreeNode(6)
	# root.left.right.left = _TreeNode(999)
	root.right.left = _TreeNode(5)
	root.right.right = _TreeNode(8)
	return root

def pre_order_iter(root):
	aStack = [(root, 1)]
	aList = []
	while aStack:
		node, count = aStack.pop()
		if count == 1:
			aList.append(node.value)
			aStack.append((node, count + 1))
			if node.left:
				aStack.append((node.left, 1))
		if count == 2:
			aStack.append((node, count + 1))
			if node.right:
				aStack.append((node.right, 1))
		if count == 3:
			continue
	print(aList)

def pre_order_traverse(root):
	res = []
	pre_order_traverse_helper(root, res)
	print(res)

def pre_order_traverse_helper(cur, res):
	if not cur:
		return
	res.append((cur.value, cur.left_total, cur.right_total))
	pre_order_traverse_helper(cur.left, res)
	pre_order_traverse_helper(cur.right, res)

def in_order_iter(root):
	aStack = [(root, 1)]
	aList = []
	while aStack:
		node, count = aStack.pop()
		if count == 1:
			aStack.append((node, count + 1))
			if node.left:
				aStack.append((node.left, 1))
		if count == 2:
			aList.append(node.value)
			aStack.append((node, count + 1))
			if node.right:
				aStack.append((node.right, 1))
		if count == 3:
			continue
	print(aList)

def in_order_traverse(root):
	res = []
	in_order_traverse_helper(root, res)
	print(res)

def in_order_traverse_helper(cur, res):
	if not cur:
		return
	in_order_traverse_helper(cur.left, res)
	res.append(cur.value)
	in_order_traverse_helper(cur.right, res)

def post_order_iter(root):
	aStack = [(root, 1)]
	aList = []
	while aStack:
		node, count = aStack.pop()
		if count == 1:
			aStack.append((node, count + 1))
			if node.left:
				aStack.append((node.left, 1))
		if count == 2:
			aStack.append((node, count + 1))
			if node.right:
				aStack.append((node.right, 1))
		if count == 3:
			aList.append(node.value)
	print(aList)

def post_order_traverse(root):
	res = []
	post_order_traverse_helper(root, res)
	print(res)

def post_order_traverse_helper(cur, res):
	if not cur:
		return
	post_order_traverse_helper(cur.left, res)
	post_order_traverse_helper(cur.right, res)
	res.append(cur.value)

def get_tree_height(curr):
	if not curr:
		return 0
	return 1 + max(get_tree_height(curr.left), get_tree_height(curr.right))

def get_tree_size(curr):
	if not curr:
		return 0
	left = get_tree_size(curr.left)
	right = get_tree_size(curr.right)

	return 1 + left + right

def traverse_by_level(root):
	curr = [root]
	next = []
	line = []
	while curr:
		curr_node = curr.pop(0)
		if curr_node.left:
			next.append(curr_node.left)
		if curr_node.right:
			next.append(curr_node.right)
		line.append(curr_node.value)
		if not curr:
			print(line)
			line = []
			if next:
				curr = next
				next = []

def upside_down(root):
	# Given a binary tree where all the right nodes are either leaf nodes with a sibling or empty
	# flip upside down and the original right node is left node right now
	# 	     1                         4
	# 	   / \             	         / \
	#     2  3                      5  2
	# 	/ \                           / \
	#  4  5                          3  1
	if not root:
		return root
	if not root.left and not root.right:
		return root
	new_root = upside_down(root.left)
	root.left.left = root.right
	root.left.right = root
	root.left = None
	root.right = None
	return new_root

def longest_consec(root, par, longest_length_at_par):
	if not root:
		return longest_length_at_par
	size = 1
	if par and root.value == par.value + 1:
		size = longest_length_at_par + 1
	return max(longest_length_at_par, longest_consec(root.left, root, size), longest_consec(root.right, root, size))

def num_of_left_node(curr_node):
	if not curr_node:
		return 0
	left = num_of_left_node(curr_node.left)
	right = num_of_left_node(curr_node.right)
	curr_node.left_total = left
	return 1 + left + right

def num_of_right_node(curr_node):
	if not curr_node:
		return 0
	left = num_of_right_node(curr_node.left)
	right = num_of_right_node(curr_node.right)
	curr_node.right_total = right
	return 1 + left + right

def is_BST_1_helper(root):
	pass
def is_BST_1(root):
	pass


a = random_tree()
num_of_left_node(a)
num_of_right_node(a)
# print(get_tree_size(a))
# pre_order_traverse(a)
# pre_order_iter(a)
# in_order_traverse(a)
# in_order_iter(a)
# post_order_traverse(a)
# post_order_iter(a)
# traverse_by_level(a)
# print(longest_consec(a, None, 0))
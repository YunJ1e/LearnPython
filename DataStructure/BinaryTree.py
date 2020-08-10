"""
Updated: 2020/08/10
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
	root = _TreeNode(10)
	root.left = _TreeNode(5)
	root.right = _TreeNode(15)
	root.left.left = _TreeNode(2)
	root.left.right = _TreeNode(7)
	root.left.right.left = _TreeNode(999)
	root.right.left = _TreeNode(-12)
	root.right.right = _TreeNode(-20)
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

def get_max_depth_helper(root):
	if not root:
		return -float("inf")
	if not root.left and not root.right:
		return 1

	left = get_max_depth_helper(root.left)
	right = get_max_depth_helper(root.right)

	return max(left, right) + 1

def get_max_depth(root):
	# This is for the case that the root is None
	if not root:
		return 0
	return get_max_depth_helper(root)

def get_min_depth_helper(root):
	if not root:
		return float("inf")
	if not root.left and not root.right:
		return 1

	left = get_min_depth_helper(root.left)
	right = get_min_depth_helper(root.right)

	return min(left, right) + 1

def get_min_depth(root):
	# This is for the case that the root is None
	if not root:
		return 0
	return get_min_depth_helper(root)

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

def is_BST_1_helper(root, prev):
	if not root:
		return True
	if not is_BST_1_helper(root.left, prev):
		return False
	if prev[0] >= root.value:
		return False
	prev[0] = root.value
	return is_BST_1_helper(root.right, prev)

def is_BST_1(root):
	prev = [-float("inf")]
	return is_BST_1_helper(root, prev)

def is_BST_2_helper(root):
	if not root:
		return True, None, None
	lr, lmin, lmax = is_BST_2_helper(root.left)
	rr, rmin, rmax = is_BST_2_helper(root.right)
	return lr and rr and (not lmax or lmax < root.value) and (not rmin or rmin > root.value), \
		lmin or root.value, \
		rmax or root.value

def is_BST_2(root):
	return is_BST_2_helper(root)

def max_path_sum_leaf_to_root(root):
	# Given a binary tree in which each node contains an integer number.
	# Find the maximum possible path sum from a leaf to root.
	if not root:
		return -float("inf")
	if not root.left and not root.right:
		return root.value

	left = max_path_sum_leaf_to_root(root.left)
	right = max_path_sum_leaf_to_root(root.right)
	return max(left, right) + root.value

def max_path_sum_to_target_leaf_to_root(root, curr_sum, target):
	if not root:
		return False

	if not root.left and not root.right:
		return curr_sum + root.value == target

	return max_path_sum_to_target_leaf_to_root(root.left, curr_sum + root.value, target) \
		or max_path_sum_to_target_leaf_to_root(root.right, curr_sum + root.value, target)

def max_path_node_to_node_helper(root, max_for_now):
	global res
	if not root:
		return
	if max_for_now < 0:
		max_for_now = root.value
	else:
		max_for_now += root.value
	res = max(max_for_now, res)

	max_path_node_to_node_helper(root.left, max_for_now)
	max_path_node_to_node_helper(root.right, max_for_now)

def max_path_node_to_node(root):
	global res
	res = root.value
	max_path_node_to_node_helper(root, 0)
	print(res)

def max_path_sum_leaf_to_leaf_helper(root):
	global res
	max_path_sum_leaf_to_leaf(root)
	print(res)

def max_path_sum_leaf_to_leaf(root):
	global res
	if not root:
		return 0
	if not root.left and not root.right:
		return root.value

	left = max_path_sum_leaf_to_leaf(root.left)
	right = max_path_sum_leaf_to_leaf(root.right)

	if root.left and root.right:
		res = max(res, left + right + root.value)
		return max(left, right) + root.value
	else:
		return root.value + right if root.left else root.value + left

def max_path_sum_helper(root):
	global res
	if not root:
		return 0
	left = max_path_sum_helper(root.left)
	right = max_path_sum_helper(root.right)

	left = 0 if left < 0 else left
	right = 0 if right < 0 else right

	res = max(res, left + right + root.value)
	return max(left, right, 0) + root.value

def max_path_sum(root):
	global res
	max_path_sum_helper(root)
	print(res)

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
traverse_by_level(a)
# print(longest_consec(a, None, 0))
print(is_BST_1(a))
print(is_BST_2(a))
print(get_min_depth_helper(a))
print(get_max_depth_helper(a))
print(max_path_sum_to_target_leaf_to_root(a, 0, 20))
max_path_node_to_node(a)
max_path_sum_leaf_to_leaf_helper(a)
res = 0
max_path_sum(a)
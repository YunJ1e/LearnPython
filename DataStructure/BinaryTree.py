"""
Updated: 2020/07/30
Author: Yunjie Wang
"""
class _TreeNode(object):
	def __init__(self, x):
		self.value = x
		self.left = None
		self.right = None

class Binary_Tree(object):
	def __init__(self):
		self.root = None

	def random_tree(self):
		self.root = _TreeNode(10)
		self.root.left = _TreeNode(5)
		self.root.right = _TreeNode(15)
		self.root.left.left = _TreeNode(2)
		self.root.left.right = _TreeNode(7)
		# self.root.right.left = _TreeNode(12)
		# self.root.right.right = _TreeNode(20)

	def pre_order_traverse(self):
		res = []
		self.pre_order_traverse_helper(self.root, res)
		print(res)

	def pre_order_traverse_helper(self, cur, res):
		if not cur:
			return
		res.append(cur.value)
		self.pre_order_traverse_helper(cur.left, res)
		self.pre_order_traverse_helper(cur.right, res)

	def in_order_traverse(self):
		res = []
		self.in_order_traverse_helper(self.root, res)
		print(res)

	def in_order_traverse_helper(self, cur, res):
		if not cur:
			return
		self.in_order_traverse_helper(cur.left, res)
		res.append(cur.value)
		self.in_order_traverse_helper(cur.right, res)

	def post_order_traverse(self):
		res = []
		self.post_order_traverse_helper(self.root, res)
		print(res)

	def post_order_traverse_helper(self, cur, res):
		if not cur:
			return
		self.post_order_traverse_helper(cur.left, res)
		self.post_order_traverse_helper(cur.right, res)
		res.append(cur.value)

	def get_tree_height(self, curr):
		if not curr:
			return 0
		return 1 + max(self.get_tree_height(curr.left), self.get_tree_height(curr.right))

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







a = Binary_Tree()
a.random_tree()
a.pre_order_traverse()
a.in_order_traverse()
a.post_order_traverse()
print(a.get_tree_height(a.root))
traverse_by_level(a.root)
b = upside_down(a.root)
traverse_by_level(b)

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

a = Binary_Tree()
a.root = _TreeNode(10)
a.root.left = _TreeNode(5)
a.root.right = _TreeNode(15)
a.root.left.left = _TreeNode(2)
a.root.left.right = _TreeNode(7)
a.root.right.left = _TreeNode(12)
a.root.right.right = _TreeNode(20)
a.pre_order_traverse()
a.in_order_traverse()
a.post_order_traverse()

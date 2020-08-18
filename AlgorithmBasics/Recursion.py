"""
Updated: 2020/08/18
Author: Yunjie Wang
"""

import random

"""
Recursion
"""


def loop_fib(n):
	# The function is to calculate the n-th fibonacci number
	# By definition, the fibonacci numbers are 0, 1, 1, 2, 3, 5 etc
	if n <= 1:
		return n
	a = 0
	b = 1
	for i in range(1, n):
		temp = b
		b += a
		a = temp
	return b


def recur_fib(n):
	if n <= 1:
		return n
	return recur_fib(n - 1) + recur_fib(n - 2)


class CakeRecipe(object):
	"""
	The class is a toy model for the multi-stage problems, which could be solved easier with the help
	of the so-called backtracking(DFS) method
	"""

	def __init__(self):
		"""
		Assume that a cake is made of three ingredients, and it only contains one from each type.
		"""
		self.creams = ["c1", "c2", "c3"]
		self.flours = ["f1", "f2"]
		self.fruits = ["fr1", "fr2", "fr3", "fr4"]
		self.recipes = []

	def make_cake(self):
		"""
		The function stores each type of ingredients as a list and put all of them in the list
		And triggers the first call of the backtracking
		:return: None
		"""
		ingredients = [self.creams, self.flours, self.fruits]
		recipe = []
		self.bt(recipe, ingredients)

	def bt(self, recipe, ingredients):
		"""
		The function starts the recursion for the backtracking
		:param recipe:
		:param ingredients:
		:return:
		"""
		# If the type of the ingredients we choose is equal to those we have,
		# it means we have a complete recipe done. And we keep a copy of it.
		if len(recipe) == len(ingredients):
			self.recipes.append(recipe[:])
			return

		for ingredient in ingredients[len(recipe)]:
			recipe.append(ingredient)
			self.bt(recipe, ingredients)
			recipe.pop()

	def __str__(self):
		res = "There are {0} recipes for a cake\n".format(len(self.recipes))
		res += "-"*20
		for recipe in self.recipes:
			res += "\n"
			res += ", ".join(recipe)

		return res

# a = CakeRecipe()
# a.make_cake()
# print(a)


class Permutation(object):
	"""
	The class provides permutation algorithms for different cases with the help of the backtracking
	"""
	def __init__(self):
		self.nums = ["a", "c", "b", "d"]
		self.perms = []

	def distinct_bt(self, partial_perm):
		"""
		The function starts the recursion for the backtracking
		:param partial_perm: The permutation that is partially filled
		:return:
		"""
		if len(partial_perm) == len(self.nums):
			self.perms.append(partial_perm[:])
			return
		for num in self.nums:
			if num not in partial_perm:
				# To avoid the repetition of a number
				partial_perm.append(num)
				self.distinct_bt(partial_perm)
				partial_perm.pop()
		return

	def optimized_distinct_bt(self, stage):
		"""
		The function starts the recursion for the backtracking
		Previous one has a extra search complexity when checking whether the num is used before
		So, in order to further decrease the complexity, I just use the original list swapping to get
		the ideal result.
		Besides I need a extra variable to track the stage of swap
		:param partial_perm: The permutation that is partially filled
		:return:
		"""
		if stage == len(self.nums):
			self.perms.append(self.nums[:])
			return
		for i in range(stage, len(self.nums)):
			self.nums[i], self.nums[stage] = self.nums[stage], self.nums[i]
			self.optimized_distinct_bt(stage + 1)
			self.nums[i], self.nums[stage] = self.nums[stage], self.nums[i]
		return

	def perm_call(self):
		perm = []
		if random.randint(0, 1):
			self.distinct_bt(perm)
		else:
			print("Optimized")
			self.optimized_distinct_bt(0)

	def __str__(self):
		res = "There are {0} permutations for the number list [{1}]\n".format(len(self.perms), ", ".join(self.nums))
		res += "-"*20
		for perm in self.perms:
			res += "\n"
			res += ", ".join(perm)
		return res

# a = Permutation()
# a.perm_call()
# print(a)


class Subset(object):
	"""
	The class provides algorithms for generating possible subsets with the help of the backtracking
	"""
	def __init__(self):
		self.nums = ["a", "b", "c", "d"]
		self.subsets = []

	def subset_call(self):
		subset = []
		self.subset_bt(subset, 0)

	def subset_bt(self, subset, stage):
		"""
		For every element in the list, there are two options, choose or not choose
		And since the length of the subset is not necessarily represent the stage of choosing, we need an extra number
		:param subset: Current subset
		:param stage: Current stage of the finding subsets
		:return: None
		"""
		if stage == len(self.nums):
			self.subsets.append(subset[:])
			return
		# Not choose
		self.subset_bt(subset, stage + 1)
		# Choose
		subset.append(self.nums[stage])
		self.subset_bt(subset, stage + 1)
		subset.pop()
		return

	def __str__(self):
		res = "There are {0} permutations for the list [{1}]\n".format(len(self.subsets), ", ".join(self.nums))
		res += "-"*20
		for subset in self.subsets:
			res += "\n"
			res += ", ".join(subset)
		return res


# a = Subset()
# a.subset_call()
# print(a)


class ValidParentheses(object):
	"""
	The class provides algorithms for generating valid parentheses with the help of the backtracking
	"""
	def __init__(self):
		self.num_of_pairs = 4
		self.valid_pairs = []

	def parentheses_call(self):
		valid_pair = []
		self.parentheses_bt(valid_pair)

	def parentheses_bt(self, valid_pair):
		if len(valid_pair) == 2 * self.num_of_pairs:
			self.valid_pairs.append(valid_pair[:])
		if valid_pair.count("(") < self.num_of_pairs:
			# There are ('s left to use
			valid_pair.append("(")
			self.parentheses_bt(valid_pair)
			valid_pair.pop()

		if self.is_left_parentheses_unmatched(valid_pair):
			valid_pair.append(")")
			self.parentheses_bt(valid_pair)
			valid_pair.pop()


	def is_left_parentheses_unmatched(self, sequence):
		"""
		The functions checks whether there are left parentheses unmatched
		:param sequence: Parentheses Sequence
		:return: None
		"""
		s = []
		for seq in sequence:
			if seq == "(":
				s.append(seq)
			else:
				s.pop()
		return len(s) > 0

	def __str__(self):
		res = "There are {0} valid combinations for {1} pairs of parentheses\n".format(len(self.valid_pairs), self.num_of_pairs)
		res += "-"*20
		for pair in self.valid_pairs:
			res += "\n"
			res += "".join(pair)
		return res


a = ValidParentheses()
a.parentheses_call()
print(a)
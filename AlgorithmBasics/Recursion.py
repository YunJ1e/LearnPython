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
		self.nums = ["a", "c", "c", "c"]
		self.perms = []

	def distinct_bt(self, partial_perm):
		"""
		The function starts the recursion for the backtracking
		This one only deals with the case where the nums contains no duplicate numbers, because once there are duplicate
		numbers the base case condition will not match
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
		:param stage: A extra variable to track the stage of swap
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

	def possible_duplicate_bt(self, partial_perm):
		"""
		The function starts the recursion for the backtracking
		This one is able to deals with the case where the nums contains duplicate numbers
		At each level, the duplicate number cannot be used more than once, which can be achieved by the SET
		But in the final perm, it still is a part of the permutation
		:param partial_perm: The permutation that is partially filled
		:return:
		"""
		if len(partial_perm) == len(self.nums):
			self.perms.append(partial_perm[:])
			return
		unique_set = set()
		for num in self.nums:
			# The second condition allows duplicate numbers even they have already been in the permutation
			# But the third condition is to prevent duplicate nums in the same level
			if (num not in partial_perm or partial_perm.count(num) < self.nums.count(num)) and num not in unique_set:
				# To avoid the repetition of a number
				unique_set.add(num)
				partial_perm.append(num)
				self.possible_duplicate_bt(partial_perm)
				partial_perm.pop()
		return

	def optimized_possible_duplicate_bt(self, stage):
		"""
		The function starts the recursion for the backtracking
		Previous one has a extra search complexity when checking whether the num is used before
		So, in order to further decrease the complexity, I just use the original list swapping to get
		the ideal result.
		Besides I need a extra variable to track the stage of swap
		Also compared with the non-duplicate one, a unique set is needed for the
		:param stage: A extra variable to track the stage of swap
		:return:
		"""
		if stage == len(self.nums):
			self.perms.append(self.nums[:])
			return
		unique_set = set()
		for i in range(stage, len(self.nums)):
			if self.nums[i] not in unique_set:
				unique_set.add(self.nums[i])
				self.nums[i], self.nums[stage] = self.nums[stage], self.nums[i]
				self.optimized_possible_duplicate_bt(stage + 1)
				self.nums[i], self.nums[stage] = self.nums[stage], self.nums[i]
		return

	def perm_call(self):
		perm = []
		self.possible_duplicate_bt(perm)
		# self.optimized_possible_duplicate_bt(0)
		# if random.randint(0, 1):
		# 	self.distinct_bt(perm)
		# else:
		# 	print("Optimized")
		# 	self.optimized_distinct_bt(0)

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
		self.nums = ["a", "b", "b"]
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

		# Choose
		subset.append(self.nums[stage])
		self.subset_bt(subset, stage + 1)
		subset.pop()
		next = stage + 1
		while next < len(self.nums) and self.nums[next] == self.nums[stage]:
			stage = next
			next = stage + 1
		# Not choose
		self.subset_bt(subset, stage + 1)

		return

	def __str__(self):
		res = "There are {0} permutations for the list [{1}]\n".format(len(self.subsets), ", ".join(self.nums))
		res += "-"*len(res[:])
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
		if random.randint(0, 1):
			self.parentheses_bt(valid_pair)
		else:
			print("Optimized")
			self.optimized_parentheses_bt(valid_pair, 0, 0)

	def optimized_parentheses_bt(self, valid_pair, left, right):
		"""
		The function generates valid parentheses with the help of the backtracking
		And also reduce time complexity on checking the balance of them using extra variables
		:param valid_pair:
		:param left:
		:param right:
		:return:
		"""
		if len(valid_pair) == 2 * self.num_of_pairs:
			self.valid_pairs.append(valid_pair[:])
		if left < self.num_of_pairs:
			# There are ('s left to use
			valid_pair.append("(")
			self.optimized_parentheses_bt(valid_pair, left + 1, right)
			valid_pair.pop()

		if left > right:
			valid_pair.append(")")
			self.optimized_parentheses_bt(valid_pair, left, right + 1)
			valid_pair.pop()

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


# a = ValidParentheses()
# a.parentheses_call()
# print(a)


class Combination(object):
	"""
	The class provides several functions for different cases of combination
	"""
	def __init__(self):
		"""
		Here we assume the k is less than the length of the nums
		"""
		self.nums = ["a", "b", "c", "d", "e"]
		self.k = 2
		self.ans = []

	def combine(self):
		"""
		The function initializes conditions for backtracking
		:return:
		"""
		comb = []
		stage = 0
		count = 0
		self.combine_bt(comb, stage, count)

	def combine_bt(self, comb, stage, count):
		"""
		Backtrack function, once the stage reaches the k, the current comb will be joined as string and put into ans
		:param comb:
		:param stage:
		:return:
		"""
		if stage == self.k:
			self.ans.append("".join(comb))
			return

		for i in range(stage + count, len(self.nums)):
			comb.append(self.nums[i])

			self.combine_bt(comb, stage + 1, count)
			count += 1
			comb.pop()

	def __str__(self):
		res = "There are {0} valid combinations choosing {1} numbers from [{2}] \n".format(len(self.ans), self.k, ", ".join(self.nums))
		res += "-"*20
		for pair in self.ans:
			res += "\n"
			res += pair
		return res


# a = Combination()
# a.combine()
# print(a)


class Coins(object):
	"""
	The class includes functions that solves the "combinations of coins" problem
	"""
	def __init__(self):
		self.target = 4
		self.coins_options = [2, 1]
		self.result = []

	def coins_combination(self):
		comb = []
		self.coin_comb_bt(comb, self.target, 0)
		print(self.result)

	def coin_comb_bt(self, comb, target, coin_index):
		if len(comb) == len(self.coins_options):
			if target == 0:
				self.result.append(comb[:])
			return

		for i in range(target // self.coins_options[coin_index] + 1):
			comb.append(i)
			self.coin_comb_bt(comb, target - i * self.coins_options[coin_index], coin_index + 1)
			comb.pop()




a = Coins()
a.coins_combination()
# print(a)

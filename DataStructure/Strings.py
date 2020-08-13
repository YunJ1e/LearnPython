"""
Updated: 2020/08/13
Author: Yunjie Wang
"""


class StringOperation(object):
	def __init__(self, input_str):
		self._input_string = input_str
		self._output_string = None

	def set_input(self, input_str):
		self._input_string = input_str

	def get_input(self):
		return self._input_string

	def _set_output(self, res):
		self._output_string = res

	def get_output(self):
		return self._output_string

	def _remove_helper(self, remove_list):
		"""
		The function removes certain char(s) from the input string
		:return: The string after the removal
		"""
		string_list = list(self._input_string)
		fast = 0
		slow = 0
		while fast < len(string_list):
			if string_list[fast] not in remove_list:
				string_list[slow] = string_list[fast]
				slow += 1
			fast += 1
		self._set_output("".join(string_list[:slow]))

	def remove(self, remove_list):
		"""
		The function removes certain char(s) from the input string
		:return: None
		"""
		self._remove_helper(remove_list)

	def _remove_spaces(self):
		"""
		The function removes the leading and trailing spaces and also the duplicate spaces inside the string
		:return: None
		"""
		if not self._input_string:
			return self._input_string
		string_list = list(self._input_string)
		fast, slow = 0, 0
		while fast < len(string_list):
			# As long as the char in the fast position is not space, the list has to be updated
			# "or" The number before the slow position is not space and the slow position itself is not the beginning
			if string_list[fast] != " " or (slow != 0 and string_list[slow - 1] != " "):
				string_list[slow] = string_list[fast]
				slow += 1
			fast += 1
		# If there are several trailing spaces, the algorithm above will keep one.
		if slow > 0 and string_list[slow - 1] == " ":
			slow -= 1

		self._set_output("".join(string_list[:slow]))

	def remove_spaces(self):
		"""
		The function removes the leading and trailing spaces and also the duplicate spaces inside the string
		:return:None
		"""
		self._remove_spaces()

	def _remove_duplicate(self):
		"""
		The function removes the duplicate in the string ans
		:return:
		"""
		string_list = list(self._input_string)
		fast, slow = 1, 1
		while fast < len(string_list):
			if string_list[fast] != string_list[slow - 1]:
				string_list[slow] = string_list[fast]
				slow += 1
			fast += 1
		self._set_output("".join(string_list[:slow]))

	def remove_duplicate(self):
		"""
		The function removes the duplicate in the string
		:return:
		"""
		self._remove_duplicate()

	def _remove_duplicate_repeat(self):
		"""
		The functions removes the duplicated char from the string repeatedly ans change the output string
		:return: None
		"""
		if not self._input_string or len(self._input_string) < 2:
			self._set_output(self._input_string)

		string_list = list(self._input_string)
		fast = 0
		aStack = []
		while fast < len(string_list):
			# When there is nothing in the stack we need to append one element
			# "or" the element on the fast position is equal to the one on the top the stack
			if len(aStack) > 0 and string_list[fast] == aStack[-1]:
				# It is possible that there are some duplicated following
				while fast < len(string_list) and string_list[fast] == aStack[-1]:
					fast += 1
				aStack.pop()
			else:
				aStack.append(string_list[fast])
				fast += 1
		self._set_output("".join(aStack))

	def remove_duplicate_repeat(self):
		"""
		The functions removes the duplicated char from the string repeatedly
		:return: None
		"""
		self._remove_duplicate_repeat()

	def _reverse_string(self, string_list, left, right):
		"""
		The function reverse the string in the list
		:return: None
		"""
		while left < right:
			string_list[left], string_list[right] = string_list[right], string_list[left]
			left += 1
			right -= 1

	def _reverse_string_by_word(self):
		"""
		The function reverses the string, "I love Python" -> "Python love I"
		:return: None
		"""
		string_list = list(self._input_string)
		self._reverse_string(string_list, 0, len(string_list) - 1)
		fast, slow = 0, 0
		i = 0
		while i < len(string_list):
			if i == len(string_list) - 1 or string_list[i + 1] == " ":
				fast = i
				self._reverse_string(string_list, slow, fast)
				slow = i + 2
			i += 1

		self._set_output("".join(string_list))

	def reverse_string_by_word(self):
		"""
		The function reverses the string, "I love Python" -> "Python love I"
		:return: None
		"""
		self._reverse_string_by_word()

	def _is_sub_string(self, pattern):
		"""
		The functions determines whether the given string is a substring of the input string
		:return: None
		"""
		if len(self._input_string) < len(pattern):
			self._set_output("Not a substring")
		for i in range(len(self._input_string) - len(pattern) + 1):
			if pattern == self._input_string[i:i + len(pattern)]:
				self._set_output("is a substring")
				return
		self._set_output("Not a substring")



	def is_sub_string(self, pattern):
		"""
		The functions determines whether the given string is a substring of the input string
		:return: None
		"""
		# Brute Force
		self._is_sub_string(pattern)

	def __str__(self):
		res = "Input: {0}\nOutput: {1}\n".format(self.get_input(), self.get_output())
		res += "-"*20
		return res

# Test Code
a = StringOperation("  s   t u de nt   ")
a.remove_spaces()
print(a)

a.set_input("student")
a.remove(["u"])
print(a)

a.set_input("aabbssddccasd")
a.remove_duplicate()
print(a)

a.set_input("abbbaz")
a.remove_duplicate_repeat()
print(a)

a.set_input("I love Python")
a.reverse_string_by_word()
print(a)

a.set_input("student")
a.is_sub_string("tuda")
print(a)

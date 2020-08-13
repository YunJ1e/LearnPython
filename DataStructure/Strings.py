"""
Updated: 2020/08/12
Author: Yunjie Wang
"""

class string_opeartion(object):
	def __init__(self, input_str):
		self.input_string = input_str
		self.output_string = None

	def _remove_helper(self):
		"""
		The function removes certain char(s) from the input string
		:return: The string after the removal
		"""
		string_list = list(self.input_string)
		fast = 0
		slow = 0
		while fast < len(string_list):
			if string_list[fast] not in ["n", "u"]:
				string_list[slow] = string_list[fast]
				slow += 1
			fast += 1
		return "".join(string_list[:slow])

	def remove(self):
		"""
		The function removes certain char(s) from the input string
		:return: None
		"""
		self.output_string = self._remove_helper()

a = string_opeartion("student")
a.remove()
print(a.output_string)
"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/02
Author: Yunjie Wang
"""

"""
Problem 30 (443839)
"""
def num_to_digit(num):
	str_num = str(num)
	res = 0
	for digit in str_num:
		# print(int(digit) ** 4)
		res += int(digit) ** 5
	return res

def func030():
	# There is a certain range in which
	# the sum of largest digit fifth power is smaller than the smallest number in that range
	order = 1
	while order * 9**5 > 10 ** (order - 1):
		order += 1
	j = 0
	for i in range(2, 10 **(order - 1)):
		if i == num_to_digit(i):
			j += i
			print(i)
	print(j)


func030()
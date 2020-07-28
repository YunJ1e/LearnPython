"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/28
Author: Yunjie Wang
"""

"""
Problem 14 (837799)
"""

def collatz_sequence(num):
	count = 1
	num_list = [str(num)]
	if num < 13:
		return

	while num != 1:
		if num % 2 == 0:
			num = num // 2
			num_list.append(str(num))
		else:
			num = 3 * num + 1
			num_list.append(str(num))
		count += 1

	return count, num_list

def func014():
	max_count = 0
	max_len_list = []
	for i in range(13, 1000001):
		counter, col_seq = collatz_sequence(i)
		if counter > max_count:
			max_count = counter
			max_len_list = col_seq
			# print(max_count, max_seq)

	print(max_len_list[0])

func014()
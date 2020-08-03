"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/03
Author: Yunjie Wang
"""

"""
Problem 31 (73682)
"""

def divide(num, divisors):
	count = 0
	for i in range(0, num // divisors[0] + 1):
		new_num = num - i * divisors[0]
		for j in range(0, new_num // divisors[1] + 1):
			new_num = num - i * divisors[0] - j * divisors[1]
			for k in range(0, new_num // divisors[2] + 1):
				new_num = num - i * divisors[0] - j * divisors[1] - k * divisors[2]
				for m in range(0, new_num // divisors[3] + 1):
					new_num = num - i * divisors[0] - j * divisors[1] - k * divisors[2] - m * divisors[3]
					for n in range(0, new_num // divisors[4] + 1):
						new_num = num - i * divisors[0] - j * divisors[1] - k * divisors[2] - m * divisors[3] - n * divisors[4]
						for l in range(0, new_num // divisors[5] + 1):
							new_num = num - i * divisors[0] - j * divisors[1] - k * divisors[2] - m * divisors[3] - \
							          n * divisors[4] - l * divisors[5]
							for a in range(0, new_num // divisors[6] + 1):
								new_num = num - i * divisors[0] - j * divisors[1] - k * divisors[2] - m * divisors[3] - \
								          n * divisors[4] - l * divisors[5] - a * divisors[6]
								if i * divisors[0] + j * divisors[1] + k * divisors[2] + m * divisors[3] + n * divisors[4] + l * divisors[5] + a * divisors[6] == num:
									count += 1
									# print(i, j, k, m, n, l, a)
	# + 1 is for the case when only using 200
	return count + 1


divide(200, [100, 50, 20, 10, 5, 2, 1])
"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/06
Author: Yunjie Wang
"""

"""
Problem 40 (210)
"""

def find_fraction_digit(num, nth_digit):
	return abs(int((num - int(num)) * (10**nth_digit)) - int((num - int(num)) * (10**(nth_digit - 1))) * 10)

def generate_irrational():
	num = ""
	i = 1
	while len(num) < 1000000:
		num += str(i)
		i += 1
	return num
# generate_irrational()

def func040():
	aNum = generate_irrational()
	res = 1
	for i in range(7):
		res *= int(aNum[10 ** i - 1])
	print(res)

func040()
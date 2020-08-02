"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/01
Author: Yunjie Wang
"""

"""
Problem 27 (-59231)
"""

def euler_consec_prime():
		return form_equation(-79, 1601)

# For the value of c, we can narrow it down, because c itself has to be a prime for the case that x = 0

def is_prime(num):
	# Check whether or not it can be divided by the 2 ans some corner cases
	# By definition, 1 is not a prime number
	if num == 1 or num == 0:
		return False
	if num == 2:
		return True
	if num % 2 == 0:
		return False
	# The number for sure is a odd one from now
	for i in range(3, num, 2):
		if num % i == 0:
			return False
	return True

def form_equation(a, b):
	i = 0
	while i >= 0:
		num = i * i + a * i + b
		if not is_prime(abs(num)):
			# print(i)
			return i
		i += 1

def find_the_num_of_prime():
	b_list = [False] * 1001
	for i in range(len(b_list)):
		b_list[i] = is_prime(i)
	a_max, b_max = -999,  -1000
	max_num = 0
	for i in range(-999, 1000, 2):
		for j in range(-1000, 1001):
			if b_list[abs(j)]:
				count = form_equation(i, j)
				if count > max_num:
					max_num = count
					a_max, b_max = i, j
	print(a_max, b_max, max_num, a_max * b_max)

find_the_num_of_prime()
# print(form_equation(1, 1), form_equation(-79, 1601))

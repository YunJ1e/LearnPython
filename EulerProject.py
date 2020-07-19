"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/19
Author: Yunjie Wang
"""
import math
"""
Problem 1 (233168)
"""
def func001():
	target_list = []
	for i in range(1, 1000):
		if (i % 3) == 0 or (i % 5) == 0:
			target_list.append(i)
	result = sum(target_list)
	print(result)
# func001()

"""
Problem 2 (4613732)
"""
def func002():
	upper_limit = 4000000
	x = 1
	y = 2
	sum = 0
	while x <= upper_limit:
		if x % 2 == 0:
			sum += x
		temp = y
		y = x + y
		x = temp
	print(sum)
# func002()

"""
Problem 3 (6857)
"""
def max_prime_factor(num):
	max_prime = -1
	# The largest possible factor
	sqrt_num = int(math.sqrt(num))

	# If the number is divisible only by 2,
	# the result will be 2.
	# Otherwise it will break out the while loop
	# And the num right now cannot be divided by 2 any more
	while num % 2 == 0:
		max_prime = 2
		num = num // 2
	# The possible factor start from 3, end at sqrt_num
	# because the num cannot be divided by 2 any more, choose step to be 2
	for i in range(3, sqrt_num + 1, 2):
		while num % i == 0:
			max_prime = i
			num = num // i
	if num > max_prime:
		max_prime = num

	return max_prime
# print(max_prime_factor(600851475143))

"""
Problem 4 (906609)
"""
def number_list(num):
	digit_list = []
	while num != 0:
		digit_list.append(num % 10)
		num = num // 10
	return digit_list

def reverse_num(num):
	nums_list = number_list(num)
	list_length = len(nums_list)
	result = 0
	for i in range(list_length):
		result += nums_list[list_length - i - 1] * (10 ** i)
	return result

def max_palindrome_product(ndigit):
	# using string manipulation would be easier than complete number operation
	# The number range of that digit
	lower_bound = 10**(int(ndigit) - 1)
	upper_bound = 10**(int(ndigit)) - 1
	result = 0
	for i in range(upper_bound, lower_bound - 1, -1):
		for j in range(upper_bound, lower_bound - 1, -1):
			product_result = i * j
			mirror_result = reverse_num(product_result)
			if mirror_result == product_result and product_result > result:
				result = product_result
	return result
# print(max_palindrome_product(3))

"""
Problem 5(232792560)
"""
def least_comment_multiplier(n):
	result = 1
	for i in range(1, n+1):
		result = int(result * i / math.gcd(result, i))
	return result
# print(least_comment_multiplier(20))
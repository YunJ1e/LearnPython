"""
Euler Project
Started: 2020/07/18
Updated: 2020/08/04
Author: Yunjie Wang
"""

"""
Problem 33 ()
"""

def num_check(num, den):
	one_num = num % 10
	one_den = den % 10
	ten_num = num // 10
	ten_den = den // 10

	# There are only 4 possible situations
	# 1. one_num = one_den & num/ den = ten_num / ten_den
	# 2. one_num = ten_den & num/ den = ten_num / one_den
	# 3. ten_num = one_den & num/ den = one_num / ten_den
	# 4. ten_num = ten_den & num/ den = one_num / one_den

	if (one_num == one_den and num * ten_den == ten_num * den) or (one_num == ten_den and num * one_den == ten_num * den) or (ten_num == one_den and num * ten_den == one_num * den) or (ten_num == ten_den and num * one_den == one_num * den):
		return True

def func033():
	import math
	res_numer = 1
	res_deno = 1
	for deno in range(10, 100):
		for numer in range(10, deno):
			if (deno % 10) and (numer % 10) and num_check(numer, deno):
				res_numer *= numer
				res_deno *= deno
	print(res_deno // math.gcd(res_numer, res_deno))

func033()

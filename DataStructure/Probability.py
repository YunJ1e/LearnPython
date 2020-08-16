"""
Updated: 2020/08/16
Author: Yunjie Wang
"""

# Use of certain library to achieve some probabilistic methods

import random


def shuffle(input_list):
	"""
	The function gives one of the permutations of the list randomly
	As we know, the perfect shuffle algorithm will give one specific permutation with the probability of 1/(# of element)!
	:param input_list: The list we need to shuffle
	:return: The shuffled list
	"""

	length = len(input_list)
	for i in range(length - 1, -1, -1):
		random_num = random.randint(0, i)
		input_list[random_num], input_list[i] = input_list[i], input_list[random_num]
	print(input_list)


def reservoir_sample(sample, n, value):
	"""
	The function implements the reservoir sampling algorithm - reading part
	:param sample: The original sample
	:param n: Indicates the "value" is the n-th in the data stream
	:param value: Actual value in the data stream
	:return: tuple of the new sample and the "n" as a counter
	"""
	r = random.randint(0, n - 1)
	if r == 0:
		sample = value
	return sample, n + 1


def new_random(m, n):
	"""
	The function generate 0 ~ n-1 integers using randint(0, m-1)
	:param m: The random function m we have
	:param n: The random function n we need to build
	:return: randint(0,n-1)
	"""
	digit = 0
	cur = n
	while cur > 0:
		cur = cur // m
		digit += 1
	while True:
		sum = 0
		for i in range(digit):
			sum = sum * m + random.randint(0, m - 1)
		if sum < n:
			return sum


print(new_random(2, 1000))
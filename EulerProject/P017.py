"""
Euler Project
Started: 2020/07/18
Updated: 2020/07/29
Author: Yunjie Wang
"""

"""
Problem 17 (21124)
"""

def seperate_the_number(num):
	# Only up to 1000
	magni = 1
	digit_list = []
	while num > 0:
		digit = num % (10 ** magni)
		digit_list.append(digit)
		num = num // (10 ** magni)
	return digit_list

def read_the_number(num):
	ONES = [
		"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten",
		"eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen","nineteen"]
	TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
	if 0 <= num <= 19:
		return ONES[num]
	elif 20 <= num <= 99:
		return TENS[num // 10] + (ONES[num % 10] if num % 10 != 0 else "")
	elif 1000 <= num < 1000000:
		return read_the_number(num // 1000) + "thousand" + (read_the_number(num % 1000) if (num % 1000 != 0) else "")
	else:
		return ONES[num // 100] + "hundred" + (("and" + read_the_number(num % 100)) if (num % 100 != 0) else "")

def compare_the_len():
	max_length = 0
	for i in range(1, 1001):
			max_length += len(read_the_number(i))
	return max_length

print(compare_the_len())
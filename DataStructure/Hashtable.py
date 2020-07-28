"""
Updated: 2020/07/22
Author: Yunjie Wang
"""
"""
In the Python, the general hashtable is implemented by the built-in feature dictionary
"""

# Count word occurrences in a word array
def count_occurrences(wordList):
	freqs = {}
	for word in wordList:
		if word not in freqs:
			freqs[word] = 1
		else:
			freqs[word] += 1
	return freqs

def unique_element(word):
	u_set = set()
	for letter in word:
		u_set.add(letter)
	return u_set

def count_the_digit(digit, num_dict, aString):
	if not num_dict:
		num_dict[str(digit)] = 1
	elif str(digit) not in num_dict:
		aKey, freq = list(num_dict.items())[0]
		aString += str(freq)
		aString += aKey
		num_dict.clear()
		num_dict[str(digit)] = 1
	else:
		num_dict[str(digit)] += 1
	return aString

def count_and_say(n):
	# Given a sequence of number: 1, 11, 21, 1211, 111221, …
	#
	# The rule of generating the number in the sequence is as follow:
	#   1 is "one 1" so 11.
	#   11 is "two 1s" so 21.
	#   21 is "one 2 followed by one 1" so 1211.
	#   Find the nth number in this sequence.
	#
	# Assumptions:
	# 	n starts from 1, the first number is "1", the second number is "11" n is smaller than 30
	count = 1
	num_string = "1"
	num_string_speak = "1"
	while count in range(1, n):
		num_dict = {}
		num_string_speak = ""
		for i in num_string:
			num_string_speak = count_the_digit(i, num_dict, num_string_speak)
		aKey, freq = list(num_dict.items())[0]
		num_string_speak += str(freq)
		num_string_speak += aKey
		num_string = num_string_speak
		count += 1
	print(num_string_speak)

# count_and_say(10)

def miss_num(array):
	"""
	Given an integer array of size N - 1, containing all the numbers from 1 to N except one, find the missing number.
	Assumptions
		The given array is not null, and N >= 1
	Examples
		A = {2, 1, 4}, the missing number is 3
		A = {1, 2, 3}, the missing number is 4
		A = {}, the missing number is 1
	"""
	N = len(array) + 1
	aSet = {i for i in range(1, N + 1)}
	return list(aSet - set(array))[0]

def bubble_sort_tuple(a_list, b_list):
	# Based on the a_list, bubble sort both of them
	for i in range(len(a_list) - 1):
		for j in range(i + 1, len(a_list)):
			if a_list[j] > a_list[i]:
				a_list[j], a_list[i] = a_list[i], a_list[j]
				b_list[j], b_list[i] = b_list[i], b_list[j]

def top_k_frequent_words(Composition, K):
	"""
	Given a composition with different kinds of words, return a list of the top K most frequent words in the composition.
	Assumptions
		the composition is not null and is not guaranteed to be sorted
		K >= 1 and
		K could be larger than the number of distinct words in the composition, in this case, just return all the distinct words
	Return:
		a list of words ordered from most frequent one to least frequent one (the list could be of size K or smaller than K)
	Examples
		Composition = ["a", "a", "b", "b", "b", "b", "c", "c", "c", "d"], top 2 frequent words are [“b”, “c”]
		Composition = ["a", "a", "b", "b", "b", "b", "c", "c", "c", "d"], top 4 frequent words are [“b”, “c”, "a", "d"]
		Composition = ["a", "a", "b", "b", "b", "b", "c", "c", "c", "d"], top 5 frequent words are [“b”, “c”, "a", "d"]
	"""

	count_dict = {}
	for element in Composition:
		if element not in count_dict:
			count_dict[element] = 1
		else:
			count_dict[element] += 1
	alp_list = []
	count_list = []
	for item in count_dict:
		alp_list.append(item)
		count_list.append(count_dict[item])
	bubble_sort_tuple(count_list,alp_list)

	if K not in range(1, len(alp_list)):
		return alp_list
	else:
		return alp_list[:K]

print(top_k_frequent_words(["a", "a", "b", "b", "b", "b", "c", "c", "c", "d"], 10))
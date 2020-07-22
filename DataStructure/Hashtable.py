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


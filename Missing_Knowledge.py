"""
Updated: 2020/07/12
Author: Yunjie Wang
"""

"""
This file includes some basic Python knowledge I miss when I first learn Python
1. Difference Between Continue and Break (Line 18)
2. Passing by Reference, and the return of the function (Line 38)
3. OOP (Line 81)
4. Draw the Dynamics (Line 137)
"""
"""
Difference Between Continue and Break
"""


def continue_or_break():
	"""
	See the difference between continue and break
	Break will end the entire loop,
	instead the continue only skips the current iteration.
	"""
	# Will stop printing when meeting the space between first and last name
	for letter in "Yunjie Wang":
		if letter == " ":
			break
		print(letter, end="")

	print()
	# Will skip the space between first and last name
	for letter in "Yunjie Wang":
		if letter == " ":
			continue
		print(letter, end="")


"""
Passing by Reference...
"""


def foo1(x):
	x.append(1)
	x = [2]
	x.append(1)
	return x


def foo2(x):
	x.append(1)
	x.append(1)
	x = [2]
	return x


def foo3(x):
	x = [2]
	x.append(1)
	x.append(1)
	return x


def call_foo():
	x = [0]
	y = foo1(x)
	#Expected: [0,1], [2,1]
	print(x, y)

	x = [0]
	y = foo2(x)
	# Expected: [0,1,1], [2]
	print(x, y)

	x = [0]
	y = foo3(x)
	# Expected: [0], [2,1,1]
	print(x, y)


"""
OOP
"""


class ListNode(object):
	def __init__(self, value):
		self.next = None
		self.val = value


def print_all_nodes(headNode):
	while headNode is not None:
		print(headNode.val, "->", end=" ")
		headNode = headNode.next
	print("None")


def merge_two_sorted_llist(headOne, headTwo):
	# Handle the corner cases, if one of them is empty, return the other(regardless empty or not)
	if headOne is None:
		return headTwo
	if headTwo is None:
		return headOne
	# General Case
	current = ListNode(None)
	newHead = current
	while headOne and headTwo:
		if headOne.val < headTwo.val:
			# When the value of the headOne is less than headTwo, we move on to compare the next on in the llist
			smallHead = headOne
			headOne = headOne.next
		else:
			smallHead = headTwo
			headTwo = headTwo.next
		current.next = smallHead
		current = current.next
	# Once they get out the while loop(at least one of them is empty)
	if headOne:
		current.next = headOne
	else:
		current.next = headTwo

	return newHead.next


def test_merge():
	llist_01 = ListNode(1)
	llist_01.next = ListNode(3)
	llist_02 = ListNode(2)
	print_all_nodes(llist_01)
	print_all_nodes(llist_02)
	newLlist = merge_two_sorted_llist(llist_01, llist_02)
	print_all_nodes(newLlist)


"""
Draw the Dynamics
https://towardsdatascience.com/intro-to-dynamic-visualization-with-python-animations-and-interactive-plots-f72a7fb69245
"""


def fermi(E: float, E_f: float, T: float) -> float:
	import numpy as np
	k_b = 8.617 * (10**-5) # eV/K
	return 1/(np.exp((E - E_f)/(k_b * T)) + 1)


def static_plot_the_data():
	import numpy as np
	import matplotlib as mpl
	import matplotlib.pyplot as plt

	# General plot parameters
	# I find sometimes these statements are confusing when you first look
	# Especially you are not familiar with the maplotlib
	# mpl.rcParams['font.family'] = 'serif'
	# mpl.rcParams['font.size'] = 10
	# mpl.rcParams['axes.linewidth'] = 2
	# mpl.rcParams['axes.spines.top'] = False
	# mpl.rcParams['axes.spines.right'] = False
	# mpl.rcParams['xtick.major.size'] = 10
	# mpl.rcParams['xtick.major.width'] = 2
	# mpl.rcParams['ytick.major.size'] = 10
	# mpl.rcParams['ytick.major.width'] = 2

	# Create figure and add axes
	fig = plt.figure(figsize=(6, 4))
	ax = fig.add_subplot(111)

	# Temperature values
	T = np.linspace(100, 1000, 10)

	# Get colors from coolwarm colormap
	colors = plt.get_cmap('coolwarm', 10)

	# Plot F-D data
	for i in range(len(T)):
		x = np.linspace(0, 1, 100)
		y = fermi(x, 0.5, T[i])
		ax.plot(x, y, color=colors(i), linewidth=2.5)

	# Add legend
	labels = ['100 K', '200 K', '300 K', '400 K', '500 K', '600 K',
	          '700 K', '800 K', '900 K', '1000 K']
	ax.legend(labels, loc='upper right',
	          frameon=False, labelspacing=0.2)
	plt.show()

# continue_or_break()
# call_foo()
# plot_the_data()

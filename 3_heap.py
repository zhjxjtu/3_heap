""" 
Solution for all winning points of 3 heap cards game
Winning point starts from (1, 1, 1)
Result shows all the number combo less than pow(2, RANK)
"""

from __future__ import print_function

RANK = 3 # Fee free to ++ to see bigger result pool

int_max = 2**RANK # Max number based on RANK

# Convert a integer to binary list
def int_to_bin_list(int_num): 
	bin_list = list('{0:0b}'.format(int_num))
	length = len(bin_list)
	while length > 0:
		bin_list[length-1] = int(bin_list[length-1])
		length -= 1
	less = RANK - len(bin_list)
	while (less > 0):
		bin_list.insert(0, 0)
		less -= 1
	return bin_list

# Print if the current combo is a winning point
def print_if_wp(a, b, c):
	bin_a = int_to_bin_list(a)
	bin_b = int_to_bin_list(b)
	bin_c = int_to_bin_list(c)
	mod_2 = 0
	i = 0
	for i in range(0, RANK):
		mod_2 += (bin_a[i] + bin_b[i] + bin_c[i]) % 2
		i += 1
	if mod_2 == 0:
		print(a, b, c)

# Traverse all the combination and test if it is a winning point
def trav():
	a = b = c = 1 # Initial minimium winning point = 1,1,1
	print('Winning points for numbers <', int_max)
	print(1, 1, 1)
	for a in range(1, int_max):
		for b in range(a, int_max):
			for c in range(b, int_max):
				print_if_wp(a, b, c)
				c += 1
			b += 1
		a += 1

trav()
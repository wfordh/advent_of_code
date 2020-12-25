"""
Advent of Code 2020
Day: 18
Puzzle: 1
Language: Python
"""

from ast import literal_eval
import re

def do_calcs(exp_list):
	res = 0
	for idx, elem in enumerate(exp_list):
		if idx == 0:
			res += int(elem)
		if elem == "*":
			res *= int(exp_list[idx + 1])
		elif elem == "+":
			res += int(exp_list[idx + 1])
	return str(res)

def reduce_parens(exp):
	# need to work on nested parens
	# move while in here??
	exp_copy = exp
	while "(" in exp_copy:
		exp_match = re.search(r"^\(.*?\)", exp_copy).group()
		# keep the match
		print(exp_match)
		# this is subbing all of them and we only want to sub the outer most set
		# m = re.sub(r"[\(\)]", "", exp_match).split()
		exp_copy = exp_match.lstrip("(").strip(")")
		print(exp_copy)
	# need to find innermost paren before doing this
	new_sub = do_calcs(exp_copy.split())
	# replace the match
	return exp.replace(exp_match, new_sub)


def main():
	# use literal_eval...doesn't work for mult
    infile_path = "../../../data/2020_day_18.txt"
    with open(infile_path, "r") as infile:
    	data = [x.strip() for x in infile.readlines()]

    result = 0
    foo = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
    print(foo)
    while "(" in foo:
    	print(foo)
    	foo = reduce_parens(foo)

    print(foo)
    print(do_calcs(foo.split())) # won't work with mult left over?


if __name__ == '__main__':
	main()
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
	# does not work if more than two terms within parens
	# ^ still struggling here
	exp_match = re.search(r"\(\d+ [+*] \d+\)", exp).group()
	# keep the match
	print(exp_match)
	m = re.sub(r"[\(\)]", "", exp_match).split()
	print(m)
	new_sub = do_calcs(m)
	# replace the match
	return exp.replace(exp_match, new_sub)


def main():
	# use literal_eval...doesn't work for mult
    infile_path = "../../../data/2020_day_18.txt"
    with open(infile_path, "r") as infile:
    	data = [x.strip() for x in infile.readlines()]

    result = 0
    foo = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
    print(foo)
    while "(" in foo:
    	print(foo)
    	foo = reduce_parens(foo)

    print(foo)
    print(do_calcs(foo.split())) # won't work with mult left over?

    # search for parens with matching close parens
    # get operator
    # do operation
    # return result with parens removed

if __name__ == '__main__':
	main()
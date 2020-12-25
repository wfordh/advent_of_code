"""
Advent of Code 2020
Day: 18
Puzzle: 1
Language: Python
"""

from ast import literal_eval
import re

def reduce_parens(exp):
	exp_match = re.search(r"\(\d+ [+*] \d+\)", exp).group()
	# keep the match
	print(exp_match)
	m = re.sub(r"[\(\)]", "", exp_match).split()
	if m[1] == "*":
		new_sub = str(int(m[0])*int(m[2]))
	else:
		new_sub = str(int(m[0])+int(m[2])) # literal_eval()?
	print(new_sub)
	# replace the match
	return exp.replace(exp_match, new_sub)


def main():
	# use literal_eval...doesn't work for mult
    infile_path = "../../../data/2020_day_18.txt"
    with open(infile_path, "r") as infile:
    	data = [x.strip() for x in infile.readlines()]

    result = 0
    foo = '2 * 3 + (4 * 5)'
    print(foo)
    while "(" in foo:
    	print(foo)
    	foo = reduce_parens(foo)

    print(foo)
    print(literal_eval(foo)) # won't work with mult left over?

    # search for parens with matching close parens
    # get operator
    # do operation
    # return result with parens removed

if __name__ == '__main__':
	main()
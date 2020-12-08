"""
Advent of Code 2020
Day: 7
Puzzle: 1
Language: Python
"""

import re


def main():
	infile_path = "../../../data/2020_day_7.txt"
	with open(infile_path, "r") as infile:
		data = [x.strip() for x in infile.readlines()]

	bag_colors = dict()

	for bag in data:
		bag_info = bag.split("bags contain")
		base_bag = bag_info[0].strip()
		try:
			bag_contains = {
				re.search(r"\d (.*?) bag", sub_bag).group(1).strip():int(re.search(r"(\d)", sub_bag).group(1))
				for sub_bag in bag_info[1].split(",")
			}
		except AttributeError:
			bag_contains = 0
		bag_colors[base_bag] = bag_contains

	num_bags = list()
	stack = bag_colors["shiny gold"].copy()
	print(stack)
	# recursive algo?
	for bag, contained_bags in stack.items():
		queue = list(bag_colors[bag].keys())
		this_bag = [contained_bags]
		while queue:
			current = queue.pop(0)
			print(current)
			if bag[current] > 0:
				print(bag[current])
				this_bag.append(contained_bags[current])
				# queue.insert()




if __name__ == '__main__':
	main()
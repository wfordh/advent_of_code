"""
Advent of Code 2020
Day: 9
Puzzle: 1
Language: Python
"""

from itertools import combinations

def main():
	infile_path = "../../../data/2020_day_09.txt"
	with open(infile_path, "r") as infile:
		data = [int(line.strip()) for line in infile.readlines()]

	is_found = False
	idx = 0
	while not is_found:
		# idx = idx % len(data) # how to do this?
		elements = data[idx:idx+25]
		target = data[idx+25]
		combos = combinations(elements, 2)
		num_successes = 0
		for combo in list(combos):
			if sum(combo) == target:
				num_successes += 1
				break
		if num_successes == 0:
			print(target)
			is_found = True
		idx += 1


if __name__ == '__main__':
	main()
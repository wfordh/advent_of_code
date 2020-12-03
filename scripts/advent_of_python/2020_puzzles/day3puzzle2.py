"""
Advent of Code 2020
Day: 3
Puzzle: 2
Language: Python
"""
from functools import reduce

def slope_run(data, step_down, step_right):
	num_trees = 0
	i = j = 0
	while i < len(data):
		if j >= len(data[0]):
			j = j % len(data[0])
		if data[i][j] == "#":
			num_trees += 1
		i += step_down
		j += step_right
	return num_trees

def main():
	infile_path = "../../../data/2020_day_3.txt"
	with open(infile_path, "r") as infile:
		data = infile.readlines()
		data = [x.strip() for x in data]

	
	slopes_to_try = [
		(1, 1),
		(1, 3),
		(1, 5),
		(1, 7),
		(2, 1)
	]

	results = [slope_run(data, x, y) for x, y in slopes_to_try]
	print(reduce(lambda x, y: x*y, results))


if __name__ == '__main__':
	main()
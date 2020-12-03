"""
Advent of Code 2020
Day: 3
Puzzle: 1
Language: Python
"""

# incorrect guesses: 10, 73, 74

def main():
	infile_path = "../../../data/2020_day_3.txt"
	with open(infile_path, "r") as infile:
		data = infile.readlines()
		data = [x.strip() for x in data]

	num_trees = 0
	i = j = 0
	while i < len(data):
		if j >= len(data[0]):
			j = j % len(data[0])
		if data[i][j] == "#":
			num_trees += 1
		i += 1
		j += 3
	print(num_trees)


if __name__ == '__main__':
	main()
"""
Advent of Code 2020
Day: 6
Puzzle: 2
Language: Python
"""

# Incorrect guess: 4761

def main():
	infile_path = "../../../data/2020_day_6.txt"
	with open(infile_path, "r") as infile:
		data = list()
		current = list()
		for line in infile:
			if line.strip() == "":
				data.append(current)
				current = list()
			else:
				current.append(line.strip())
		data.append(current)

	num_all_yes = 0
	for point in data:
		common_yes = set("abcdefghijklmnopqrstuvwxyz")
		while point:
			current = point.pop()
			common_yes = common_yes.intersection(current)
		num_all_yes += len(common_yes)

	print(num_all_yes)


if __name__ == '__main__':
	main()
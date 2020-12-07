"""
Advent of Code 2020
Day: 6
Puzzle: 1
Language: Python
"""

def main():
	infile_path = "../../../data/2020_day_6.txt"
	with open(infile_path, "r") as infile:
		data = list()
		current = list()
		for line in infile:
			if line.strip() == "":
				data.append(current)
				current = ""
			else:
				current += line.strip()
		data.append(current)

	num_yes = 0
	for point in data:
		num_yes += len(set(point))

	print(num_yes)

if __name__ == '__main__':
	main()
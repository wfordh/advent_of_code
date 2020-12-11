"""
Advent of Code 2020
Day: 9
Puzzle: 2
Language: Python
"""

# Incorrect guesses: 381470484944974

def main():
	infile_path = "../../../data/2020_day_09.txt"
	with open(infile_path, "r") as infile:
		data = [int(line.strip()) for line in infile.readlines()]

	target = 258585477
	is_found = False

	while data and not is_found:
		current_sum = 0
		sublist = list()
		for elem in data:
			current_sum += elem
			sublist.append(elem)
			if current_sum == target:
				print(min(sublist) + max(sublist))
				is_found = True
			elif current_sum > target:
				break
		data.pop(0)

if __name__ == '__main__':
	main()

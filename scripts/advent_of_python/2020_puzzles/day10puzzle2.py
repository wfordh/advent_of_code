"""
Advent of Code 2020
Day: 10
Puzzle: 2
Language: Python
"""

# Incorrect AND way inefficient: for test 1, got 6 instead of 8

def check_jolt_diffs(elem_one, elem_two, counter):
	if elem_two - elem_one == 1:
		return (counter[0]+1, counter[1])
	elif elem_two - elem_one == 3:
		return (counter[0], counter[1]+1)

def main():
	infile_path = "../../../data/2020_day_10.txt"
	with open(infile_path, "r") as infile:
		data = [int(line.strip()) for line in infile.readlines()]

	sorted_data = sorted(data)

	solutions = list()
	solutions.append(sorted_data)

	for soln in solutions:
		for idx, elem in enumerate(soln):
			try:
				if soln[idx+1] - soln[idx-1] < 3:
					temp = soln.copy()
					temp.remove(elem)
					if temp not in solutions:
						solutions.append(temp)
			except IndexError:
				pass

	num_good = 0
	while solutions:
		current = solutions.pop()
		list_one = current.copy()
		list_two = current.copy()
		target = max(current) + 3
		list_one.insert(0, 0)
		list_two.append(target)
		num_bad = 0
		for x, y in zip(list_one, list_two):
			if y - x > 3:
				num_bad += 1
		if num_bad == 0:
			num_good += 1

	print(num_good)

if __name__ == '__main__':
	main()
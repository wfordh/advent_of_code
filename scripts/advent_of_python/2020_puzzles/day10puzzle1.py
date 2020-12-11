"""
Advent of Code 2020
Day: 10
Puzzle: 1
Language: Python
"""

def check_jolt_diffs(elem_one, elem_two, counter):
	if elem_two - elem_one == 1:
		return (counter[0]+1, counter[1])
	elif elem_two - elem_one == 3:
		return (counter[0], counter[1]+1)

def main():
	infile_path = "../../../data/2020_day_10.txt"
	with open(infile_path, "r") as infile:
		data = [int(line.strip()) for line in infile.readlines()]

	target = max(data) + 3
	sorted_data = sorted(data)
	list_one = sorted(data)
	list_two = sorted(data)

	list_one.insert(0, 0)
	list_two.append(target)
	num_one_jolt_diffs = 0
	num_three_jolt_diffs = 0

	for x, y in zip(list_one, list_two):
		if y - x == 3:
			num_three_jolt_diffs += 1
		elif y - x == 1:
			num_one_jolt_diffs += 1

	print(num_one_jolt_diffs * num_three_jolt_diffs)

	jolt_diff_counter = (0, 0)

	# this version is missing one (the last?) three diff
	for idx, elem in enumerate(sorted_data):
		if idx == 0:
			jolt_diff_counter = check_jolt_diffs(0, elem, jolt_diff_counter)
		elif idx == len(sorted_data):
			jolt_diff_counter = check_jolt_diffs(elem, elem+3, jolt_diff_counter)
		else:
			elem_one = sorted_data[idx - 1]
			jolt_diff_counter = check_jolt_diffs(elem_one, elem, jolt_diff_counter)

	print(jolt_diff_counter)
	print(jolt_diff_counter[0] * jolt_diff_counter[1])

if __name__ == '__main__':
	main()
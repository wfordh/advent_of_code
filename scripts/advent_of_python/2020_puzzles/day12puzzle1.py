"""
Advent of Code 2020
Day: 12
Puzzle: 1
Language: Python
"""

direction_map = {
	0: "E",
	90: "N",
	180: "W",
	270: "S",
}

def follow_instruction(instruction, position, direction):
	action = instruction[0]
	mvmt = int(instruction[1:])
	if action == "N":
		new_posn = (position[0], position[1] + mvmt)
		return new_posn, direction
	elif action == "S":
		new_posn = (position[0], position[1] - mvmt)
		return new_posn, direction
	elif action == "E":
		new_posn = (position[0] + mvmt, position[1])
		return new_posn, direction
	elif action == "W":
		new_posn = (position[0] - mvmt, position[1])
		return new_posn, direction
	elif action == "L":
		new_dir = direction + mvmt
		return position, new_dir
	elif action == "R":
		new_dir = direction - mvmt
		return position, new_dir
	else:
		# forward
		# print(direction_map[direction % 360], mvmt)
		new_instr = direction_map[direction % 360] + str(mvmt)
		return follow_instruction(new_instr, position, direction)



def main():
	infile_path = "../../../data/2020_day_12.txt"
	with open(infile_path, "r") as infile:
		data = [x.strip() for x in infile.readlines()]

	position = (0, 0)
	direction = 0

	for point in data:
		position, direction = follow_instruction(point, position, direction)

	print(abs(position[0]) + abs(position[1]))


if __name__ == '__main__':
	main()

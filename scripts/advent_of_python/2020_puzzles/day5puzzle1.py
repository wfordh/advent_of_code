"""
Advent of Code 2020
Day: 5
Puzzle: 1
Language: Python
"""

def bisection(arr, lower=True):
	if lower:
		return arr[:int(len(arr)/2)]
	else:
		return arr[int(len(arr)/2):]

def main():
	infile_path = "../../../data/2020_day_5.txt"
	with open(infile_path, "r") as infile:
		data = infile.readlines()
		data = [x.strip() for x in data]

	seat_ids = list()

	for ticket in data:
		rows = list(range(128))
		cols = list(range(8))
		ticket = list(ticket)

		while ticket:
			current = ticket.pop(0)
			if current == "F":
				rows = bisection(rows, True)
			elif current == "B":
				rows = bisection(rows, False)
			elif current == "L":
				cols = bisection(cols, True)
			else:
				cols = bisection(cols, False)
		assert len(rows) == 1
		assert len(cols) == 1
		seat_ids.append(rows[0]*8 + cols[0])

	print(max(seat_ids))


if __name__ == '__main__':
	main()
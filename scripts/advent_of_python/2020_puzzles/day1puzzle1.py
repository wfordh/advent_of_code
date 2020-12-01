"""
Advent of Code 2020
Day: 1
Puzzle: 1
Language: Python
"""


def main():
    with open("../../../data/2020_puzzle_1.txt", "r") as infile:
        data = infile.readlines()
        data = [int(point.rstrip()) for point in data]

    found_numbers = False
    target = 2020
    while data and not found_numbers:
        num_one = data.pop()
        for num_two in data:
            if num_one + num_two == target:
                print(num_one * num_two)
                found_numbers = True


if __name__ == "__main__":
    main()

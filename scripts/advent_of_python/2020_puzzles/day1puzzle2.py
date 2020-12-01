"""
Advent of Code 2020
Day: 1
Puzzle: 2
Language: Python
"""


def checksum(lst, target):
    while lst:
        num_one = lst.pop()
        for num_two in lst:
            if num_one + num_two == target:
                return num_one, num_two
    return None


def main():
    with open("../../../data/2020_puzzle_1.txt", "r") as infile:
        data = infile.readlines()
        data = [int(point.rstrip()) for point in data]

    found_numbers = False
    target = 2020
    while data and not found_numbers:
        current_num = data.pop()
        new_target = target - current_num
        results = checksum(data.copy(), new_target)
        if results:
            print(current_num * results[0] * results[1])


if __name__ == "__main__":
    main()

"""
Advent of Code 2020
Day: 16
Puzzle: 1
Language: Python
"""


import re


def main():
    # get rules as tuples ((x, y), (m, n)) and string together?
    infile_path = "../../../data/2020_day_16.txt"
    with open(infile_path, "r") as infile:
        rules = list()
        my_ticket = list()
        nearby_tix = list()

        data_block = 0
        for line in infile:
            if line.startswith("your ticket") or line.startswith("nearby tickets"):
                data_block += 1
                continue

            if line.strip() == "":
                continue

            if data_block == 0:
                rule = re.findall(r"(\d+)", line.strip())
                rules.append([int(num) for num in rule])
            elif data_block == 1:
                my_ticket.extend([int(num) for num in line.strip().split(",")])
            else:
                nearby_tix.append([int(num) for num in line.strip().split(",")])

    error = 0
    for ticket in nearby_tix:
        for number in ticket:
            success = 0
            for rule in rules:
                if (number >= rule[0] and number <= rule[1]) or (
                    number >= rule[2] and number <= rule[3]
                ):
                    success += 1
            if success == 0:
                error += number

    print(error)


if __name__ == "__main__":
    main()

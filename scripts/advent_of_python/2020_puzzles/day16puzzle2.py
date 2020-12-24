"""
Advent of Code 2020
Day: 16
Puzzle: 2
Language: Python

Incorrect guesses: 4805792588689 (high), 789039592493 (low)

Can I condense this? A lot of intermediate results.
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
    valid_tix = list()
    for ticket in nearby_tix:
        valid = True
        for number in ticket:
            success = 0
            for rule in rules:
                if (number >= rule[0] and number <= rule[1]) or (
                    number >= rule[2] and number <= rule[3]
                ):
                    success += 1
            if success == 0:
                error += number
                valid = False
        if valid:
            valid_tix.append(ticket)

    all_possibilities = list()
    for ticket in valid_tix:
        current_possibilities = list()
        for number in ticket:
            possible_posn = set()
            for idx, rule in enumerate(rules):
                if (number >= rule[0] and number <= rule[1]) or (
                    number >= rule[2] and number <= rule[3]
                ):
                    possible_posn.add(idx)
            current_possibilities.append(possible_posn)
        all_possibilities.append(current_possibilities)

    posn_list = list()
    for i in range(len(rules)):
        posn_sets = [poss[i] for poss in all_possibilities]
        posn = set.intersection(*posn_sets)
        posn_list.append(posn)

    sorted_posn_list = sorted(enumerate(posn_list), key = lambda x: len(x[1]))

    final_posn = list()
    seen = set()
    for idx, posn in sorted_posn_list:
        current = (posn - seen).pop()
        seen.add(current)
        # idx is position in ticket, current is position in rules
        final_posn.append((idx, current))

    result = 1
    for idx, posn in final_posn:
        if posn < 6:
            result *= my_ticket[idx]
    print(result)


if __name__ == "__main__":
    main()

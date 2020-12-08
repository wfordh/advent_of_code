"""
Advent of Code 2020
Day: 7
Puzzle: 1
Language: Python
"""

import re


def main():
    infile_path = "../../../data/2020_day_7.txt"
    with open(infile_path, "r") as infile:
        data = [x.strip() for x in infile.readlines()]

    bag_colors = dict()

    for bag in data:
        bag_info = bag.split("bags contain")
        base_bag = bag_info[0].strip()
        # remove \d to include number. could then split on first space if need the number
        try:
            bag_contains = [
                re.search(r"\d (.*?) bag", sub_bag).group(1).strip()
                for sub_bag in bag_info[1].split(",")
            ]
        except AttributeError:
            bag_contains = list()  # how to do this if None?
        bag_colors[base_bag] = bag_contains

    num_contains_gold = 0
    for bag, contained_bags in bag_colors.items():
        stack = contained_bags.copy()
        found = False
        while stack and not found:
            current = stack.pop()
            if current == "shiny gold":
                num_contains_gold += 1
                found = True
            elif not current:
                pass  # don't want to extend if None
            else:
                stack.extend(bag_colors[current])

    print(num_contains_gold)


if __name__ == "__main__":
    main()

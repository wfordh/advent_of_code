"""
Advent of Code 2020
Day: 14
Puzzle: 1
Language: Python
"""

# incorrect guesses: 142232120440

import re


def add_mask(num, mask):
    res = list()
    for idx, mask_digit in enumerate(mask):
        if mask_digit == "X":
            res.append(num[idx])
        elif mask_digit == "0":
            res.append("0")
        else:
            res.append("1")

    return int("".join(res), 2)


def main():
    infile_path = "../../../data/2020_day_14.txt"
    with open(infile_path, "r") as infile:
        data = infile.readlines()

    mask = None
    mem = dict()

    for line in data:
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
        else:
            # mem
            num = bin(int(line.split("=")[1].strip()))[2:].zfill(36)
            target = int(re.search(r"\[(\d+)\]", line).group(1))
            res = add_mask(num, mask)
            mem[target] = res

    print(sum(mem.values()))


if __name__ == "__main__":
    main()

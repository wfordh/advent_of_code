"""
Advent of Code 2020
Day: 14
Puzzle: 2
Language: Python
"""

# incorrect guesses: 18133781630147 (too high)

import re
from itertools import combinations_with_replacement, permutations
from tqdm import tqdm


def add_mask(num, mask):
    res = list()
    x_idx = list()
    for idx, mask_digit in enumerate(mask):
        if mask_digit == "X":
            res.append("X")
            x_idx.append(idx)
        elif mask_digit == "0":
            res.append(num[idx])
        else:
            res.append("1")

    return res, x_idx


def floating_combos(res, x_idx):
    potentials = list()
    num_x = len(x_idx)
    # count Xs and make that many copies of the list
    combos = combinations_with_replacement(["0", "1"], num_x)
    for combo in list(combos):
        potentials.extend(set(permutations(combo, num_x)))

    all_results = list()
    for p in potentials:
        result_copy = res.copy()
        for idx, digit in zip(x_idx, p):
            result_copy[idx] = digit
        all_results.append(result_copy)
    return all_results


def convert_num(bin_num):
    return int("".join(bin_num), 2)


def main():
    infile_path = "../../../data/2020_day_14.txt"
    with open(infile_path, "r") as infile:
        data = infile.readlines()

    mask = None
    mem = dict()

    for line in tqdm(data):
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
        else:
            # mem
            num = bin(int(line.split("=")[1].strip()))[2:].zfill(36)
            target = bin(int(re.search(r"\[(\d+)\]", line).group(1)))[2:].zfill(36)
            res, x_idx = add_mask(target, mask)
            all_results = floating_combos(res, x_idx)
            for result in all_results:
                x = convert_num(result)
                mem[x] = convert_num(num)

    print(sum(mem.values()))


if __name__ == "__main__":
    main()

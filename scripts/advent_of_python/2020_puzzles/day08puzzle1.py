"""
Advent of Code 2020
Day: 8
Puzzle: 1
Language: Python
"""

# incorrect guesses: 287,


def main():
    infile_path = "../../../data/2020_day_08.txt"
    with open(infile_path, "r") as infile:
        data = infile.readlines()

    data = [x.strip() for x in data]

    idx = 0
    visited = set()
    accumulator = 0
    found_loop = False
    while not found_loop:
        current = data[idx]
        if idx in visited:
            found_loop = True
        else:
            visited.add(idx)
        action_type = current.split(" ")[0].strip()
        action_num = int(current.split(" ")[1])
        if action_type == "nop":
            idx += 1
        elif action_type == "acc":
            accumulator += action_num
            idx += 1
        else:
            idx += action_num


if __name__ == "__main__":
    main()

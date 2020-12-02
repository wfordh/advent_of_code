"""
Advent of Code 2020
Day: 2
Puzzle: 2
Language: Python
"""


def main():
    infile_path = "../../../data/2020_day_2.txt"
    with open(infile_path, "r") as infile:
        data = infile.readlines()

    data = [x.split() for x in data]
    num_valid = 0

    for point in data:
        pos_one, pos_two = [int(x) - 1 for x in point[0].split("-")]
        letter = point[1].replace(":", "")
        password = point[2]

        if (password[pos_one] == letter and password[pos_two] != letter) or (
            password[pos_two] == letter and password[pos_one] != letter
        ):
            num_valid += 1

    print(num_valid)


if __name__ == "__main__":
    main()

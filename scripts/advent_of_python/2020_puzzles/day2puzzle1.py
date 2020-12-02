"""
Advent of Code 2020
Day: 2
Puzzle: 1
Language: Python
"""


def construct_letters_dict(password):
    letters_count = dict.fromkeys(list(password), 0)
    for letter in password:
        letters_count[letter] += 1
    return letters_count


def main():
    infile_path = "../../../data/2020_day_2.txt"
    with open(infile_path, "r") as infile:
        data = infile.readlines()

    data = [x.split() for x in data]
    num_valid = 0

    for point in data:
        min_num, max_num = [int(x) for x in point[0].split("-")]
        letter = point[1].replace(":", "")
        password = point[2]

        pw_letters_count = construct_letters_dict(password)
        for pw_letter, num in pw_letters_count.items():
            if (letter == pw_letter) and (num >= min_num) and (num <= max_num):
                num_valid += 1

    print(num_valid)


if __name__ == "__main__":
    main()

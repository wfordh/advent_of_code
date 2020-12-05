"""
Advent of Code 2020
Day: 4
Puzzle: 1
Language: Python
"""

# incorrect guesses: 24, 209


def main():
    infile_path = "../../../data/2020_day_4.txt"
    with open(infile_path, "r") as infile:
        data = list()
        current = list()
        for line in infile:
            if line.strip() == "":
                data.append(current)
                current = list()
            else:
                current.append(line.strip())
        data.append(current)

    data = [" ".join(x).split() for x in data]
    passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    num_valid = 0

    for passport in data:
        passport_data = dict.fromkeys(passport_fields, None)
        for field in passport:
            k, v = field.split(":")
            passport_data[k] = v
        # passport_data = {
        # 	field.split(":")[0]:field.split(":")[1]
        # 	for field
        # 	in passport
        # }
        passport_data.pop("cid")

        if all(passport_data.values()):
            num_valid += 1

        # need to check if all fields are there, or if only cid is missing
        # if all(passport_data.values()):
        # 	num_valid += 1
        # elif passport_data["cid"] is None:
        # 	passport_data.pop("cid")
        # 	if all(passport_data.values()):
        # 		num_valid += 1
        # else:
        # 	print(passport_data, len(passport_data), "cid" in passport_data.keys())

    print(num_valid)


if __name__ == "__main__":
    main()

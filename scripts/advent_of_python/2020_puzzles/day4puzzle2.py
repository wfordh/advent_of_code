"""
Advent of Code 2020
Day: 4
Puzzle: 1
Language: Python
"""
import re


def val_byr(byr):
    if not byr:
        return 0
    if len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002:
        return 1
    return 0


def val_iyr(iyr):
    if not iyr:
        return 0
    if len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020:
        return 1
    return 0


def val_eyr(eyr):
    if not eyr:
        return 0
    if len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030:
        return 1
    return 0


def val_hgt(hgt):
    if not hgt:
        return 0
    if hgt.endswith("cm"):
        hgt = int(hgt.split("cm")[0])
        if hgt >= 150 and hgt <= 193:
            return 1
        return 0
    elif hgt.endswith("in"):
        hgt = int(hgt.split("in")[0])
        if hgt >= 59 and hgt <= 76:
            return 1
        return 0
    return 0


def val_hcl(hcl):
    if not hcl:
        return 0
    if hcl.startswith("#"):
        hcl = hcl[1:]
        if len(hcl) == 6 and len(re.sub(r"[a-f0-9]", "", hcl)) == 0:
            return 1
    return 0


def val_ecl(ecl):
    if not ecl:
        return 0
    if ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return 1
    return 0


def val_pid(pid):
    if not pid:
        return 0
    if len(pid) == 9 and len(re.sub(r"\d", "", pid)) == 0:
        return 1
    return 0


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

        results = (
            val_byr(passport_data["byr"])
            + val_iyr(passport_data["iyr"])
            + val_eyr(passport_data["eyr"])
            + val_hgt(passport_data["hgt"])
            + val_hcl(passport_data["hcl"])
            + val_ecl(passport_data["ecl"])
            + val_pid(passport_data["pid"])
        )

        if results == 7:
            num_valid += 1

    print(num_valid)


if __name__ == "__main__":
    main()

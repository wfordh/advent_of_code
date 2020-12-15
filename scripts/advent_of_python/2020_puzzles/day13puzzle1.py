"""
Advent of Code 2020
Day: 13
Puzzle: 1
Language: Python
"""


def main():
    infile_path = "../../../data/2020_day_13.txt"
    with open(infile_path, "r") as infile:
        departure_time = int(infile.readline().strip())
        buses = infile.readline().strip()

    bus_list = [int(bus) for bus in buses.split(",") if bus != "x"]
    minutes_list = [
        (int(departure_time / bus) + 1) * bus - departure_time for bus in bus_list
    ]

    min_wait = min(minutes_list)
    for bus, wait in zip(bus_list, minutes_list):
        if wait == min_wait:
            print(bus * wait)


if __name__ == "__main__":
    main()

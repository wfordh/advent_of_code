"""
Advent of Code 2020
Day: 13
Puzzle: 2
Language: Python
"""
import sys
import time


def main():
    infile_path = "../../../data/2020_day_13.txt"
    with open(infile_path, "r") as infile:
        departure_time = int(infile.readline().strip())
        buses = infile.readline().strip()

    bus_list = [bus for bus in buses.split(",")]

    timestamp = 100000000000000 - 2
    found = False
    new_bus_list = list()
    idx_list = list()
    for idx, bus in enumerate(bus_list):
        if bus != "x":
            new_bus_list.append(bus)
            idx_list.append(idx)

    first_bus = int(bus_list[0])
    print(new_bus_list)
    print(idx_list)

    # from: https://gist.github.com/joshbduncan/65f810fe821c7a3ea81a1f5a444ea81e
    start = time.time()
    t, step = 0, 1
    for idx, bus in zip(idx_list, new_bus_list):
        while (t + idx) % int(bus) != 0:
            t += step
            print(f"current time: {t}")
        else:
            print(t, idx, bus)
        step *= int(bus)
        print(f"current step: {step}")

    print(t)
    print(time.time() - start)
    sys.exit(0)

    """
	This (my) solution works on the smaller examples but takes at least 6000x
	as long and so should not be used. 
	"""
    while not found:
        timestamp += 1
        if timestamp % 100000000000 == 1:
            print(timestamp)
        if timestamp % first_bus != 0:
            continue
        else:
            for idx, bus in zip(idx_list, new_bus_list):
                if (timestamp + idx) % int(bus) != 0:
                    timestamp += int(bus)
                    break
                if len(bus_list) - 1 == idx:
                    found = True

    print(timestamp)


if __name__ == "__main__":
    main()

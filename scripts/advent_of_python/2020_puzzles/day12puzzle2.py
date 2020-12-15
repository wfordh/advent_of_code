"""
Advent of Code 2020
Day: 12
Puzzle: 2
Language: Python
"""


def follow_instruction(instruction, ship_posn, waypoint_posn):
    action = instruction[0]
    mvmt = int(instruction[1:])
    if action == "N":
        new_wp_posn = (waypoint_posn[0], waypoint_posn[1] + mvmt)
        return ship_posn, new_wp_posn
    elif action == "S":
        new_wp_posn = (waypoint_posn[0], waypoint_posn[1] - mvmt)
        return ship_posn, new_wp_posn
    elif action == "E":
        new_wp_posn = (waypoint_posn[0] + mvmt, waypoint_posn[1])
        return ship_posn, new_wp_posn
    elif action == "W":
        new_wp_posn = (waypoint_posn[0] - mvmt, waypoint_posn[1])
        return ship_posn, new_wp_posn
    elif action == "L":
        if mvmt == 90:
            new_wp_posn = (-waypoint_posn[1], waypoint_posn[0])
        elif mvmt == 180:
            new_wp_posn = (-waypoint_posn[0], -waypoint_posn[1])
        else:
            new_wp_posn = (waypoint_posn[1], -waypoint_posn[0])
        return ship_posn, new_wp_posn
    elif action == "R":
        if mvmt == 270:
            new_wp_posn = (-waypoint_posn[1], waypoint_posn[0])
        elif mvmt == 180:
            new_wp_posn = (-waypoint_posn[0], -waypoint_posn[1])
        else:
            new_wp_posn = (waypoint_posn[1], -waypoint_posn[0])
        return ship_posn, new_wp_posn
    else:
        # forward
        new_ship_posn = (
            ship_posn[0] + mvmt * waypoint_posn[0],
            ship_posn[1] + mvmt * waypoint_posn[1],
        )
        return new_ship_posn, waypoint_posn


def main():
    infile_path = "../../../data/2020_day_12.txt"
    with open(infile_path, "r") as infile:
        data = [x.strip() for x in infile.readlines()]

    ship_posn = (0, 0)
    waypoint_posn = (10, 1)

    for pt in data:
        ship_posn, waypoint_posn = follow_instruction(pt, ship_posn, waypoint_posn)

    print(abs(ship_posn[0]) + abs(ship_posn[1]))


if __name__ == "__main__":
    main()

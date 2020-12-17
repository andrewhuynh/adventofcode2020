

def manhattan_distance(file):
    f = open(file)
    instructions_raw = f.readlines()
    f.close()

    east = 0
    north = 0
    directions = ["N","E","S","W"]
    direction = 1
    for line in instructions_raw:
        action = line[0]
        # print(action)
        units_moved = int(line.strip()[1:])
        # print(units_moved)
        if action == "N":
            north += units_moved
        elif action == "S":
            north -= units_moved
        elif action == "E":
            east += units_moved
        elif action == "W":
            east -= units_moved
        elif action == "L":
            direction = int(direction - (units_moved / 90)) % 4
        elif action == "R":
            direction = int(direction + (units_moved / 90)) % 4
        elif action == "F":
            if direction == 0:
                north += units_moved
            elif direction == 1:
                east += units_moved
            elif direction == 2:
                north -= units_moved
            elif direction == 3:
                east -= units_moved
    return abs(east) + abs(north)


def manhattan_waypoint(file):
    f = open(file)
    instructions_raw = f.readlines()
    f.close()

    ship_east = 0
    ship_north = 0
    waypoint_east = 10
    waypoint_north = 1
    directions = ["N","E","S","W"]
    direction = 1
    for line in instructions_raw:
        action = line[0]
        # print(action)
        units_moved = int(line.strip()[1:])
        # print(units_moved)
        if action == "N":
            waypoint_north += units_moved
        elif action == "S":
            waypoint_north -= units_moved
        elif action == "E":
            waypoint_east += units_moved
        elif action == "W":
            waypoint_east -= units_moved
        elif action == "L":
            quarter_turns = int(units_moved / 90) % 4
            # print(quarter_turns)
            i = 0
            while i < quarter_turns:
                swap = waypoint_north
                waypoint_north = waypoint_east
                waypoint_east = swap * -1
                i += 1
        elif action == "R":
            quarter_turns = int(units_moved / 90) % 4
            # print(quarter_turns)
            j = 0
            while j < quarter_turns:
                swap = waypoint_east
                waypoint_east = waypoint_north
                waypoint_north = swap * -1
                j += 1
        elif action == "F":
            ship_east += units_moved * waypoint_east
            ship_north += units_moved * waypoint_north
    return abs(ship_east) + abs(ship_north)

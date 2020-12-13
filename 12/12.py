def one_star():
    facing = 90
    x = y = 0
    for l in f:
        instr = l[0]
        value = int(l[1:])
        if instr == "F":
            if facing % 360 == 0:
                instr = "N"
            elif facing % 360 == 90:
                instr = "E"
            elif facing % 360 == 180:
                instr = "S"
            elif facing % 360 == 270:
                instr = "W"
        if instr == "N":
            y += value
        if instr == "S":
            y -= value
        if instr == "E":
            x += value
        if instr == "W":
            x -= value
        if instr == "L":
            facing -= value
        if instr == "R":
            facing += value
    return abs(x) + abs(y)


def two_star():
    way_x = 10
    way_y = 1
    x = y = 0
    for l in f:
        instr = l[0]
        value = int(l[1:])
        if instr == "F":
            x += way_x * value
            y += way_y * value
        elif instr == "N":
            way_y += value
        elif instr == "S":
            way_y -= value
        elif instr == "E":
            way_x += value
        elif instr == "W":
            way_x -= value
        elif instr == 'L':
            while value > 0:
                way_x, way_y = -way_y, way_x
                value -= 90
        elif instr == 'R':
            while value > 0:
                way_x, way_y = way_y, -way_x
                value -= 90
    return abs(x) + abs(y)


if __name__ == '__main__':
    f = open("input").read().splitlines()
    print(one_star())
    print(two_star())

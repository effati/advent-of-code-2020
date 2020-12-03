def one_star():
    return slope_finder(3, 1)


def two_star():
    slopes = [
        slope_finder(1, 1),
        slope_finder(3, 1),
        slope_finder(5, 1),
        slope_finder(7, 1),
        slope_finder(1, 2)
    ]
    res = 1
    for slope in slopes:
        res *= slope
    return res


def slope_finder(right, down):
    trees = 0
    max_length = len(lines[0]) - 1
    pos = right
    for line in range(down, len(lines), down):
        if pos >= max_length:
            pos -= max_length
        if lines[line][pos] == "#":
            trees += 1
        pos += right
    return trees


if __name__ == '__main__':
    with open("input", "r") as f:
        lines = f.readlines()
    print(one_star())
    print(two_star())

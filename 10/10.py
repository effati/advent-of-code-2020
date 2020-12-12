def one_star():
    lines = [int(l) for l in f]
    lines.append(0)
    lines.append(max(lines) + 3)
    lines.sort()
    one_diff = 0
    three_diff = 0
    for a, b in zip(lines, lines[1:]):
        if b - a == 1:
            one_diff += 1
        elif b - a == 3:
            three_diff += 1
    return one_diff * three_diff


def two_star():
    lines = sorted([int(l) for l in f])
    return find_ways({}, lines, 0, max(lines) + 3)


def find_ways(all_ways, lines, start, end):
    k = (start, len(lines))
    if k in all_ways:
        return all_ways[k]
    ways = 0
    if end - start <= 3:
        ways += 1
    if not lines:
        return ways
    if lines[0] - start <= 3:
        ways += find_ways(all_ways, lines[1:], lines[0], end)
    ways += find_ways(all_ways, lines[1:], start, end)
    all_ways[k] = ways
    return ways


if __name__ == '__main__':
    f = open("input").read().splitlines()
    print(one_star())
    print(two_star())

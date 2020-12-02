def one_star():
    result = 0
    with open("input", "r") as f:
        lines = f.readlines()
    for line in lines:
        split = line.split(": ")
        policy = split[0].split(" ")
        password = split[1]
        limits = policy[0].split("-")
        char = policy[1]
        lb = int(limits[0])
        ub = int(limits[1])
        occ = password.count(char)
        if lb <= occ <= ub:
            result += 1
    return result


def two_star():
    result = 0
    with open("input", "r") as f:
        lines = f.readlines()
    for line in lines:
        split = line.split(": ")
        policy = split[0].split(" ")
        password = split[1]
        limits = policy[0].split("-")
        char = policy[1]
        lb = int(limits[0]) - 1
        ub = int(limits[1]) - 1
        if password[lb] == char and password[ub] != char:
            result += 1
        elif password[lb] != char and password[ub] == char:
            result += 1
    return result


if __name__ == '__main__':
    print(one_star())
    print(two_star())

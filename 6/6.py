def one_star():
    return sum([len(l) for group in open("input").read().split("\n\n") for l in set([c for c in ''.join(group.split("\n"))])])


def two_star():
    groups = open("input").read().split("\n\n")
    ans = 0
    for group in groups:
        res = 0
        tot = {}
        people = group.split("\n")
        num_of_people = len(people)
        for person in people:
            for c in person:
                if c not in tot:
                    tot[c] = 0
                tot[c] += 1
        for c in tot:
            if tot[c] == num_of_people:
                res += 1
        ans += res
    return ans


def one_liner():
    return sum([group[c] == length for group, length in [({c: ''.join(group).count(c) for c in set(''.join(group))}, len(group)) for group in [group.split("\n") for group in open("input").read().split("\n\n")]] for c in group])


def one_liner2():
    return sum(len(set.intersection(*map(set, group.splitlines()))) for group in open("input").read().split("\n\n"))


if __name__ == '__main__':
    print(one_star())
    print(two_star())
    print(one_liner())
    print(one_liner2())

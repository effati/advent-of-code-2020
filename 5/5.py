import re


def one_star():
    return max([get_id(line) for line in open("input").read().splitlines()])


def two_star():
    all_ids = []
    for line in open("input").read().splitlines():
        all_ids.append(get_id(line))
    all_ids = sorted(all_ids)
    prev_seat = all_ids[0] - 1
    for seat in all_ids:
        if seat != prev_seat + 1:
            return seat - 1
        prev_seat = seat


def one_liner():    # WIP
    all_ids = sorted([int(line[:7], 2) * 8 + int(line[7:], 2) for line in [re.sub(r"[FL]", "0", re.sub(r"[BR]", "1", line)) for line in open("input").read().splitlines()]])
    return set(range(all_ids[0], all_ids[-1])).difference(all_ids).pop()


def get_id(line):
    line = re.sub(r"[FL]", "0", line)
    line = re.sub(r"[BR]", "1", line)
    return int(line[:7], 2) * 8 + int(line[7:], 2)


if __name__ == '__main__':
    print(one_star())
    print(two_star())
    print(one_liner())

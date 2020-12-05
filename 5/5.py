import re


def one_star():
    max_id = 0
    for line in f:
        curr_id = get_id(line)
        if curr_id > max_id:
            max_id = curr_id
    return max_id


def two_star():
    all_ids = []
    for line in f:
        all_ids.append(get_id(line))
    all_ids = sorted(all_ids)
    prev_seat = all_ids[0] - 1
    for seat in all_ids:
        if seat != prev_seat + 1:
            return seat - 1
        prev_seat = seat


def get_id(line):
    line = re.sub(r"[FL]", "0", line)
    line = re.sub(r"[BR]", "1", line)
    row = int(line[:7], 2)
    col = int(line[7:], 2)
    return row * 8 + col


if __name__ == '__main__':
    f = open("input").read().splitlines()
    print(one_star())
    print(two_star())

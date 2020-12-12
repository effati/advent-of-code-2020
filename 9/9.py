from collections import deque


def one_star():
    preamble = 25
    deq = deque([int(l) for l in f[:preamble]], maxlen=preamble)
    for l in f[preamble:]:
        curr = int(l)
        okay = False
        for d in deq:
            if curr - d in deq:
                okay = True
        if not okay:
            return curr
        deq.append(curr)


def two_star(invalid_num):
    for i, start in enumerate(f):
        tot = 0
        smallest = largest = int(start)
        for l in f[i:]:
            curr = int(l)
            tot += curr
            largest = max(curr, largest)
            smallest = min(curr, smallest)
            if tot == invalid_num:
                return smallest + largest
            if tot > invalid_num:
                break


if __name__ == '__main__':
    f = open("input").read().splitlines()
    one = one_star()
    print(one)
    print(two_star(one))

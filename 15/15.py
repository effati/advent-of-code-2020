def one_star():
    return play_game(2020)


def two_star():
    return play_game(30000000)


def play_game(n):   # cleaner version
    prev, mem = f[-1], {f[n]: n + 1 for n in range(len(f))}
    for i in range(len(mem) + 1, n + 1):
        mem[prev], prev = i - 1, 0 if prev not in mem else i - 1 - mem[prev]
    return prev


def play_game_old(n):   # first solution
    mem = {f[n]: n + 1 for n in range(len(f) - 1)}
    prev = f[-1:][0]
    for i in range(len(mem) + 2, n + 1):
        if prev not in mem:
            mem[prev] = i - 1
            prev = 0
        else:
            temp_prev = prev
            prev = i - 1 - mem[prev]
            mem[temp_prev] = i - 1
    return prev


if __name__ == '__main__':
    f = [int(n) for n in "9,3,1,0,8,4".split(",")]
    print(one_star())
    print(two_star())

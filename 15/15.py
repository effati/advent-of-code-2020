def one_star():
    mem = {f[n]: n + 1 for n in range(len(f) - 1)}
    prev = f[-1:][0]
    for i in range(len(mem) + 2, 30000001):
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

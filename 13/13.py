from functools import reduce


def one_star():
    start = int(f[0])
    buses = [int(bus) for bus in f[1].split(",") if bus != "x"]
    time = start
    while True:
        for bus in buses:
            if time % bus == 0:
                return (time - start) * bus
        time += 1


def two_star():
    buses = f[1].split(",")
    bus_crt = []
    id_crt = []
    for i, bus in enumerate(buses):
        if bus != "x":
            bus_crt.append(int(bus))
            id_crt.append(int(bus) - i)
    return crt(bus_crt, id_crt)


def crt(n, a):
    res = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        res += a_i * mul_inv(p, n_i) * p
    return res % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


if __name__ == '__main__':
    f = open("input").read().splitlines()
    print(one_star())
    print(two_star())

import re
import itertools


def one_star():
    rev_mask = ""
    mem = {}
    for l in f:
        if l.startswith("mask"):
            rev_mask = l.split(" = ")[1][::-1]
            continue
        addr = re.search(r"mem\[(\d+)]", l).group(1)
        rev_value = "{0:b}".format(int(l.split(" = ")[1]))[::-1]
        filled_value = list('{message:0<36}'.format(message=rev_value))
        for i, bit in enumerate(rev_mask):
            if bit == "X":
                continue
            filled_value[i] = bit
        mem[addr] = filled_value
    return sum([int(''.join(value[::-1]), 2) for value in mem.values()])


def two_star():
    rev_mask = ""
    mem = {}
    for l in f:
        if l.startswith("mask"):
            rev_mask = l.split(" = ")[1][::-1]
            continue
        value = int(l.split(" = ")[1])
        addr = re.search(r"mem\[(\d+)]", l).group(1)
        rev_addr = "{0:b}".format(int(addr))[::-1]
        filled_addr = list('{message:0<36}'.format(message=rev_addr))
        floating_addresses = []
        for i, bit in enumerate(rev_mask):
            if bit == "X":
                floating_addresses.append(i)
            elif bit == "1":
                filled_addr[i] = bit
        if len(floating_addresses) == 0:
            mem[''.join(filled_addr)] = value
            continue
        bitmask_combinations = list(itertools.product([0, 1], repeat=len(floating_addresses)))
        for comb in bitmask_combinations:
            alt_addr = filled_addr
            for i, floating in enumerate(floating_addresses):
                alt_addr[floating] = str(comb[i])
            mem[''.join(alt_addr)] = value
    return sum(mem.values())


if __name__ == '__main__':
    f = open("input").read().splitlines()
    print(one_star())
    print(two_star())

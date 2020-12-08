def one_star():
    lines = open("input").read().splitlines()
    acc = 0
    idx = 0
    visited = set()
    while True:
        if idx in visited:
            return acc
        acc, idx = acc_calc(acc, idx, lines, visited)


def acc_calc(acc, idx, lines, visited):
    instr = lines[idx].split()[0]
    num = int(lines[idx].split()[1])
    visited.add(idx)
    if instr == "nop":
        idx += 1
    elif instr == "acc":
        acc += num
        idx += 1
    elif instr == "jmp":
        idx += num
    return acc, idx


def try_this(lines):
    acc = 0
    idx = 0
    visited = set()
    while True:
        if idx in visited:
            return -1
        if idx >= len(lines):
            return acc
        acc, idx = acc_calc(acc, idx, lines, visited)


def two_star():
    lines = open("input").read().splitlines()
    for i, line in enumerate(lines):
        instr = lines[i].split()[0]
        num = lines[i].split()[1]
        if instr == "nop":
            copy_lines = lines.copy()
            copy_lines[i] = "jmp " + num
            tried_acc = try_this(copy_lines)
            if tried_acc > 0:
                return tried_acc
        elif instr == "jmp":
            copy_lines = lines.copy()
            copy_lines[i] = "nop " + num
            tried_acc = try_this(copy_lines)
            if tried_acc > 0:
                return tried_acc


if __name__ == '__main__':
    print(one_star())
    print(two_star())

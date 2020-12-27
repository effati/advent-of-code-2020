def one_star():
    matrix = {}
    for row, line in enumerate(f):
        for col, c in enumerate(line):
            if c == active:
                matrix[(row, col, 0)] = True
            else:
                matrix[(row, col, 0)] = False
    for i in range(6):
        matrix = check_conditions(matrix)
    return sum(matrix.values())


def check_conditions(matrix):
    new_matrix = matrix.copy()
    all_x = [x[0] for x in matrix.keys()]
    all_y = [y[1] for y in matrix.keys()]
    all_z = [z[2] for z in matrix.keys()]
    for x in range(min(all_x)-1, max(all_x)+2):
        for y in range(min(all_y)-1, max(all_y)+2):
            for z in range(min(all_z)-1, max(all_z)+2):
                curr_cube = matrix.get((x, y, z), False)
                active_neighbours = 0
                for nx in (-1, 0, 1):
                    for ny in (-1, 0, 1):
                        for nz in (-1, 0, 1):
                            if nx == ny == nz == 0:
                                continue
                            if matrix.get((x+nx, y+ny, z+nz), False):
                                active_neighbours += 1
                if curr_cube and (active_neighbours < 2 or active_neighbours > 3):
                    new_matrix[(x, y, z)] = False
                if not curr_cube and active_neighbours == 3:
                    new_matrix[(x, y, z)] = True
    return new_matrix


def two_star():
    matrix = {}
    for row, line in enumerate(f):
        for col, c in enumerate(line):
            if c == active:
                matrix[(row, col, 0, 0)] = True
            else:
                matrix[(row, col, 0, 0)] = False
    for i in range(6):
        matrix = check_conditions_4d(matrix)
    return sum(matrix.values())


def check_conditions_4d(matrix):
    new_matrix = matrix.copy()
    all_x = [x[0] for x in matrix.keys()]
    all_y = [y[1] for y in matrix.keys()]
    all_z = [z[2] for z in matrix.keys()]
    all_w = [z[2] for z in matrix.keys()]
    for x in range(min(all_x)-1, max(all_x)+2):
        for y in range(min(all_y)-1, max(all_y)+2):
            for z in range(min(all_z)-1, max(all_z)+2):
                for w in range(min(all_w)-1, max(all_w)+2):
                    curr_cube = matrix.get((x, y, z, w), False)
                    active_neighbours = 0
                    for nx in (-1, 0, 1):
                        for ny in (-1, 0, 1):
                            for nz in (-1, 0, 1):
                                for nw in (-1, 0, 1):
                                    if nx == ny == nz == nw == 0:
                                        continue
                                    if matrix.get((x+nx, y+ny, z+nz, w+nw), False):
                                        active_neighbours += 1
                    if curr_cube and (active_neighbours < 2 or active_neighbours > 3):
                        new_matrix[(x, y, z, w)] = False
                    if not curr_cube and active_neighbours == 3:
                        new_matrix[(x, y, z, w)] = True
    return new_matrix


if __name__ == '__main__':
    active = "#"
    inactive = "."
    f = open("input").read().splitlines()
    print(one_star())
    print(two_star())

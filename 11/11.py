def one_star():
    state = [floor + l + floor for l in f]
    state.insert(0, floor * len(state[0]))
    state.append(floor * len(state[0]))
    while True:
        new_state = go_through_rules_part1(state)
        if count_occupied(new_state) == count_occupied(state):
            return count_occupied(new_state)
        state = new_state


def two_star():
    state = f
    while True:
        new_state = go_through_rules_part2(state)
        if count_occupied(new_state) == count_occupied(state):
            return count_occupied(new_state)
        state = new_state


def go_through_rules_part1(state):
    new_state = []
    for row_idx, row in enumerate(state):
        if row_idx == 0 or row_idx == len(state) - 1:
            new_state.append(row)
            continue
        new_row = ""
        for col, seat in enumerate(row):
            if seat == floor:
                new_row += floor
            else:
                occ_adj = occupied_adjacent_part1(state, row_idx, col)
                if seat == empty:
                    new_row += occupied if occ_adj == 0 else empty
                elif seat == occupied:
                    new_row += empty if occ_adj >= 4 else occupied
        new_state.append(new_row)
    return new_state


def occupied_adjacent_part1(state, row, col):
    adjacent = []
    col_start = col-1
    col_end = col+1
    adjacent.append(state[row-1][col_start:col_end + 1])
    adjacent.append(state[row+1][col_start:col_end + 1])
    adjacent.append(state[row][col_start] + state[row][col_end])
    return count_occupied(adjacent)


def go_through_rules_part2(state):
    new_state = []
    for row_idx, row in enumerate(state):
        new_row = ""
        for col, seat in enumerate(row):
            if seat == floor:
                new_row += floor
            else:
                occ_adj = occupied_adjacent_part2(state, row_idx, col)
                if seat == empty:
                    new_row += occupied if occ_adj == 0 else empty
                elif seat == occupied:
                    new_row += empty if occ_adj >= 5 else occupied
        new_state.append(new_row)
    return new_state


def occupied_adjacent_part2(state, row, col):
    adjacent = []
    for row_direction in (-1, 0, 1):
        for col_direction in (-1, 0, 1):
            if row_direction == col_direction == 0:
                continue
            i = 1
            while 0 <= row + row_direction * i < len(state) and 0 <= col + col_direction * i < len(state[0]):
                seat = state[row + row_direction * i][col + col_direction * i]
                if seat != floor:
                    adjacent.append(seat)
                    break
                i += 1
    return count_occupied(adjacent)


def count_occupied(state):
    return sum([l.count(occupied) for l in state])


if __name__ == '__main__':
    occupied = "#"
    empty = "L"
    floor = "."
    f = open("input").read().splitlines()
    print(one_star())
    print(two_star())

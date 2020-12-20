def one_star():
    ans = 0
    ranges = []
    for i in range(20):
        curr_ranges = f[i].split(": ")[1].split(" or ")
        ranges.append([range(int(curr_range[0]), int(curr_range[1])+1) for curr_range in
                       [curr_range.split("-") for curr_range in curr_ranges]])
    ranges = [subrange for subranges in ranges for subrange in subranges]
    for i in range(25, len(f)):
        nums = [int(n) for n in f[i].split(",")]
        for n in nums:
            invalid = True
            for curr_range in ranges:
                if n in curr_range:
                    invalid = False
            if invalid:
                ans += n
    return ans


def in_range(ranges, n):
    return set(field_name for field_name, r in ranges.items() if n in r[0] or n in r[1])


def two_star():
    field_ranges = {}
    for i in range(20):
        curr_ranges = f[i].split(": ")
        field_ranges[curr_ranges[0]] = [range(int(curr_range[0]), int(curr_range[1]) + 1) for curr_range in
                                        [curr_range.split("-") for curr_range in curr_ranges[1].split(" or ")]]

    possible_fields = [set(field_ranges.keys()) for _ in range(len(field_ranges))]

    for i in range(25, len(f)):
        ticket = [int(n) for n in f[i].split(",")]
        if all(len(in_range(field_ranges, v)) > 0 for v in ticket):
            for k, v in enumerate(ticket):
                possible_fields[k] = possible_fields[k].intersection(in_range(field_ranges, v))

    absolute_fields = ["" for _ in range(len(field_ranges))]
    fields_left = set(field_ranges.keys())
    while len(fields_left) > 0:
        for field in range(len(field_ranges)):
            if len(possible_fields[field].intersection(fields_left)) == 1:
                new_field = list(possible_fields[field].intersection(fields_left))[0]
                absolute_fields[field] = new_field
                fields_left.remove(new_field)

    ans = 1
    my_ticket = [int(n) for n in f[22].split(',')]
    for i, n in enumerate(my_ticket):
        if absolute_fields[i].startswith("departure"):
            ans *= n
    return ans


if __name__ == '__main__':
    f = open("input").read().splitlines()
    # print(one_star())
    print(two_star())

import re

required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def one_star():
    ans = 0
    f = open("input").read().splitlines()
    # f.read().split("\n\n")
    passport = set()
    for line in f:
        if line == "":
            if passport.issuperset(required):
                ans += 1
            passport = set()
            continue
        fields = line.split(" ")
        for field in fields:
            passport.add(field.split(":")[0])
    return ans


def two_star():
    ans = 0
    f = open("input").read().splitlines()
    passport = {}
    for line in f:
        if line == "":
            ans += check_valid(passport)
            passport = {}
            continue
        fields = line.split(" ")
        for field in fields:
            kv = field.split(":")
            passport[kv[0]] = kv[1]
    return ans


def check_valid(passport):
    if not set(passport.keys()).issuperset(required):
        return 0
    if (1920 > int(passport['byr']) > 2002 or
            2010 > int(passport['iyr']) > 2020 or
            2020 > int(passport['eyr']) > 2030):
        return 0
    if not re.match(r"^[0-9]+(in|cm)$", passport['hgt']):
        return 0
    if passport['hgt'].endswith("cm") and 150 > int(passport['hgt'].split("cm")[0]) > 193:
        return 0
    if passport['hgt'].endswith("in") and 59 > int(passport['hgt'].split("in")[0]) > 76:
        return 0
    if not re.match(r"^#[a-f0-9]{6}$", passport['hcl']):
        return 0
    if passport['ecl'] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return 0
    if not re.match(r"^[0-9]{9}$", passport['pid']):
        return 0

    return 1


if __name__ == '__main__':
    print(one_star())
    print(two_star())
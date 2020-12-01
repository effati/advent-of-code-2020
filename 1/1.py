def one_star():
    with open("input", "r") as f:
        numbers = set(map(int, (f.readlines())))
        for number in numbers:
            if (2020 - number) in numbers:
                return number * (2020 - number)


def two_stars():
    with open("input", "r") as f:
        numbers = set(map(int, (f.readlines())))
        numbers_list = list(numbers)
        for i in range(len(numbers_list)):
            for j in range(i, len(numbers_list)):
                num1 = int(numbers_list[i])
                num2 = int(numbers_list[j])
                if (2020 - num1 - num2) in numbers:
                    return num1 * num2 * (2020 - num1 - num2)


if __name__ == '__main__':
    print(one_star())
    print(two_stars())

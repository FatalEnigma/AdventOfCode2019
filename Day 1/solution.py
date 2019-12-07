def calculate_fuel(value):
    return (int(value) // 3) - 2


def calculate_extra_fuel(value):
    fuel = calculate_fuel(value)

    if fuel <= 0:
        return 0

    return fuel + calculate_extra_fuel(fuel)


if __name__ == '__main__':
    print("Part 1: " + str(sum(calculate_fuel(line) for line in open("input.txt"))))
    print("Part 2: " + str(sum(calculate_extra_fuel(line) for line in open("input.txt"))))

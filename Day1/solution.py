
def part1():
    return str(sum(int(int(line) / 3) - 2 for line in open("input.txt")))


def part2():
    pass


if __name__ == '__main__':
    print("Part 1: " + part1())

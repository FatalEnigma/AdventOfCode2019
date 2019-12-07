def part1():
    for x in range(264360, 746326):
        password = [int(num) for num in str(x)]
        if sorted(password) == password and \
                any([True for x in range(1, len(password)) if password[x] == password[x - 1]]):
            yield password


def part2():
    for x in range(264360, 746326):
        password = [int(num) for num in str(x)]
        if sorted(password) == password:
            s = set(password[letter] for letter in range(1, len(password)) if password[letter] == password[letter - 1])
            if any(str(x).find(str(s_let) * 3) == -1 for s_let in s):
                yield password


if __name__ == '__main__':
    print("Part 1: {0}".format(len(list(part1()))))
    print("Part 2: {0}".format(len(list(part2()))))

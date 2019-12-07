def process_wire(wire_data):
    points = [(0, 0)]
    for instruction in wire_data.split(','):
        for _ in range(int(instruction[1:])):
            if instruction[0] == 'R':
                points.append((points[-1][0] + 1, points[-1][1]))
            elif instruction[0] == 'L':
                points.append((points[-1][0] - 1, points[-1][1]))
            elif instruction[0] == 'U':
                points.append((points[-1][0], points[-1][1] + 1))
            elif instruction[0] == 'D':
                points.append((points[-1][0], points[-1][1] - 1))
    return points[1:]


def part1(inter):
    print("Part 1: {0}".format(min(abs(x) + abs(y) for (x, y) in inter)))


def part2(w1, w2, inter):
    print("Part 2: {0}".format(
        min(2 + sum(wire.index(intersect) for wire in [w1, w2]) for intersect in inter)))


if __name__ == '__main__':
    program_input = [x for x in open("input.txt").readlines()]
    wire1 = process_wire(program_input[0])
    wire2 = process_wire(program_input[1])
    intersections = set(wire1).intersection(wire2)
    part1(intersections)
    part2(wire1, wire2, intersections)

def calculate_orbits(orbit_data, planet):
    return len(orbit_data[planet]) + sum(calculate_orbits(orbit_data, planet) for planet in orbit_data[planet])


def process(input_data):
    orbit_dict = {}

    for entry in input_data:
        orbitee = entry[0]
        orbited_by = entry[1]

        if orbitee not in orbit_dict:
            orbit_dict[orbitee] = set()

        if orbited_by not in orbit_dict:
            orbit_dict[orbited_by] = set()

        orbit_dict[orbitee].add(orbited_by)
    return orbit_dict


def part2(input_data):
    orbiter_dict = {entry[1]: entry[0] for entry in input_data}
    san_orbits = list(calculate_path_to_com(orbiter_dict, 'SAN', []))
    you_orbits = list(calculate_path_to_com(orbiter_dict, 'YOU', []))
    common = set(san_orbits).intersection(set(you_orbits))

    return min(san_orbits.index(a) + you_orbits.index(a) for a in common)


def calculate_path_to_com(orbiter_dict, destination, travelled_by):
    yield orbiter_dict[destination]

    if orbiter_dict[destination] == 'COM':
        return

    yield from calculate_path_to_com(orbiter_dict, orbiter_dict[destination], travelled_by)


if __name__ == '__main__':
    program_input = [x.strip().split(')') for x in open("input.txt")]
    orbits = process(program_input)

    print("part 1: %s" % sum(calculate_orbits(orbits, planet) for planet in orbits))
    print("part 2: %s" % part2(program_input))

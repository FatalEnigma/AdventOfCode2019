import math
from termcolor import colored

IMAGE_SIZE = 25 * 6


def part1():
    min_0 = min(images, key=lambda x: x.count("0"))
    return min_0.count("1") * min_0.count("2")


def part2():
    images2 = [[image[x*25:x*25+25] for x in range(6)] for image in images]
    final_image = [['' for _ in range(25)] for _ in range(6)]

    for y in range(6):
        for x in range(25):
            for image in images2:
                if image[y][x] == '2':
                    continue

                final_image[y][x] = colored('o', color='red') if image[y][x] == '1' else colored('o', color='white')
                break

    for row in final_image:
        print(*row)


if __name__ == '__main__':
    input_data = [x for x in open('input.txt').read().strip()]
    images = [input_data[x * 150:x * 150 + IMAGE_SIZE] for x in range(math.ceil(len(input_data) / IMAGE_SIZE))]
    print("Part 1: %s" % part1())
    print("Part 2:")
    part2()

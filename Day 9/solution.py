from queue import Queue
from intcode_pc import run_program


def get_q(queue_data):
    queue = Queue(len(queue_data))
    for item in queue_data:
        queue.put(item)
    return queue


def print_q(queue):
    while not queue.empty():
        print(queue.get())


def part1():
    output = get_q([])
    run_program(program_input, get_q([1]), output)
    print_q(output)


def part2():
    output = get_q([])
    run_program(program_input, get_q([2]), output)
    print_q(output)


if __name__ == '__main__':
    program_input = [int(x) for x in open("input.txt").read().split(',')]
    print("Part 1:")
    part1()
    print("Part 2:")
    part2()

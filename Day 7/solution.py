from threading import Thread

from opcode_queues import run_program as run
from copy import copy
from itertools import permutations
from queue import Queue


def get_q(queue_data):
    queue = Queue(len(queue_data))
    for item in queue_data:
        queue.put(item)
    return queue


def part1():
    answer = max(
        run(copy(inputs), get_q([perm[4],
                                 run(copy(inputs), get_q([perm[3],
                                                          run(copy(inputs), get_q([perm[2],
                                                                                   run(copy(inputs), get_q([perm[1],
                                                                                                            run(copy(inputs), get_q([perm[0], 0]), get_q([])).get()]), get_q([])).get()]), get_q([])).get()]), get_q([])).get()]), get_q([])).get()
        for perm in permutations(range(5)))
    return answer


def part2():
    return max(run_chain(*perm) for perm in permutations(range(5, 10)))


def run_chain(*args):
    q_list = [Queue() for i in range(5)]

    for q in zip(q_list, args):
        q[0].put(q[1])

    threads = [Thread(target=run, args=(copy(inputs), q_list[i], q_list[(i+1) % 5])) for i in range(5)]

    q_list[0].put(0)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return q_list[0].get()


if __name__ == '__main__':
    inputs = [int(x) for x in open('input.txt').read().split(',')]
    print("Part 1: %s" % part1())
    print("Part 2: %s" % part2())

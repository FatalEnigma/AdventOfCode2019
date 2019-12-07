import copy
from itertools import product

HALT = 99
ADD = 1
MULTIPLY = 2


def run_program(inputs):
    instruction_pointer = 0
    exit_program = False

    while not exit_program:
        instruction = inputs[instruction_pointer]

        if instruction == HALT:
            exit_program = True
        elif instruction == ADD:
            inputs[inputs[instruction_pointer + 3]] = inputs[inputs[instruction_pointer + 1]] + inputs[
                inputs[instruction_pointer + 2]]
        elif instruction == MULTIPLY:
            inputs[inputs[instruction_pointer + 3]] = inputs[inputs[instruction_pointer + 1]] * inputs[
                inputs[instruction_pointer + 2]]
        else:
            print("Hit unknown opcode " + str(instruction))
            exit_program = True

        instruction_pointer += 4

    return inputs


def part1(inputs):
    input_copy = copy.copy(inputs)
    input_copy[1] = 12
    input_copy[2] = 2
    print(run_program(input_copy)[0])


def part2(inputs):
    found = False

    while not found:
        for noun, verb in product(range(0, 100), range(0, 100)):
            input_copy = copy.copy(inputs)
            input_copy[1] = noun
            input_copy[2] = verb
            if run_program(input_copy)[0] == 19690720:
                print(100 * noun + verb)
                return
    print("Not Found")


if __name__ == '__main__':
    program_input = [int(x) for x in open("input.txt").read().split(',')]
    part1(program_input)
    part2(program_input)

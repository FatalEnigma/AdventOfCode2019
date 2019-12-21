from collections import namedtuple
from copy import copy

OPCODE = namedtuple('OPCODE', 'opcode instruction_length')
HALT = OPCODE(99, 4)
ADD = OPCODE(1, 4)
MULTIPLY = OPCODE(2, 4)
INPUT = OPCODE(3, 2)
OUTPUT = OPCODE(4, 2)
JUMP_IF_TRUE = OPCODE(5, 3)
JUMP_IF_FALSE = OPCODE(6, 3)
LESS_THAN = OPCODE(7, 4)
EQUALS = OPCODE(8, 4)


def advance_instruction_pointer(opcode):
    return opcode.instruction_length


def resolve_parameter(inputs, parameter_value, parameter_mode):
    if parameter_mode == '0':
        return inputs[inputs[parameter_value]]
    elif parameter_mode == '1':
        return inputs[parameter_value]
    else:
        print("Unknown parameter mode: " + parameter_mode)


def run_program(inputs, manual_input=None):
    instruction_pointer = 0
    exit_program = False

    while not exit_program:
        instruction = int(str(inputs[instruction_pointer])[-2:].lstrip("0"))
        mode = str(inputs[instruction_pointer])[:-2].rjust(3, '0')

        if instruction == HALT.opcode:
            exit_program = True
        elif instruction == ADD.opcode:
            inputs[inputs[instruction_pointer + 3]] = resolve_parameter(inputs, instruction_pointer + 1, mode[-1]) + \
                                                      resolve_parameter(inputs, instruction_pointer + 2, mode[-2])
            instruction_pointer += advance_instruction_pointer(ADD)
        elif instruction == MULTIPLY.opcode:
            inputs[inputs[instruction_pointer + 3]] = resolve_parameter(inputs, instruction_pointer + 1, mode[-1]) * \
                                                      resolve_parameter(inputs, instruction_pointer + 2, mode[-2])
            instruction_pointer += advance_instruction_pointer(MULTIPLY)
        elif instruction == INPUT.opcode:
            inputs[inputs[instruction_pointer + 1]] = manual_input if manual_input else (input("What is your input?: "))
            instruction_pointer += advance_instruction_pointer(INPUT)
        elif instruction == OUTPUT.opcode:
            print(resolve_parameter(inputs, instruction_pointer + 1, mode[-1]))
            instruction_pointer += advance_instruction_pointer(OUTPUT)
        elif instruction == JUMP_IF_TRUE.opcode:
            if resolve_parameter(inputs, instruction_pointer + 1, mode[-1]) != 0:
                instruction_pointer = resolve_parameter(inputs, instruction_pointer + 2, mode[-2])
            else:
                instruction_pointer += advance_instruction_pointer(JUMP_IF_TRUE)
        elif instruction == JUMP_IF_FALSE.opcode:
            if resolve_parameter(inputs, instruction_pointer + 1, mode[-1]) == 0:
                instruction_pointer = resolve_parameter(inputs, instruction_pointer + 2, mode[-2])
            else:
                instruction_pointer += advance_instruction_pointer(JUMP_IF_FALSE)
        elif instruction == LESS_THAN.opcode:
            if resolve_parameter(inputs, instruction_pointer + 1, mode[-1]) < \
                    resolve_parameter(inputs, instruction_pointer + 2, mode[-2]):
                inputs[inputs[instruction_pointer + 3]] = 1
            else:
                inputs[inputs[instruction_pointer + 3]] = 0
            instruction_pointer += advance_instruction_pointer(LESS_THAN)
        elif instruction == EQUALS.opcode:
            if resolve_parameter(inputs, instruction_pointer + 1, mode[-1]) == \
                    resolve_parameter(inputs, instruction_pointer + 2, mode[-2]):
                inputs[inputs[instruction_pointer + 3]] = 1
            else:
                inputs[inputs[instruction_pointer + 3]] = 0
            instruction_pointer += advance_instruction_pointer(EQUALS)

        else:
            print("Hit unknown opcode " + str(instruction))
            exit_program = True

    return inputs


if __name__ == '__main__':
    program_input = [int(x) for x in open("input.txt").read().split(',')]
    print("Part 1:")
    run_program(copy(program_input), manual_input=1)
    print("Part 2:")
    run_program(copy(program_input), manual_input=5)

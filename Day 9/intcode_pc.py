from collections import namedtuple
from sys import exit

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
REL_BASE_OFFSET = OPCODE(9, 2)


def advance_instruction_pointer(opcode):
    return opcode.instruction_length


def resolve_parameter_value(inputs, parameter_value, parameter_mode, relative_base):
    if parameter_mode == '0':
        return inputs[inputs[parameter_value]]
    elif parameter_mode == '1':
        return inputs[parameter_value]
    elif parameter_mode == '2':
        return inputs[inputs[parameter_value] + relative_base]
    else:
        print("Unknown parameter mode: " + parameter_mode)


def resolve_parameter_address(inputs, parameter_value, parameter_mode, relative_base):
    if parameter_mode == '0':
        return inputs[parameter_value]
    elif parameter_mode == '1':
        print("Error write using immediate mode")
        exit(1)
    elif parameter_mode == '2':
        return inputs[parameter_value] + relative_base
    else:
        print("Unknown parameter mode: " + parameter_mode)


def run_program(inputs, input_queue, output_queue):
    instruction_pointer = 0
    relative_base = 0
    exit_program = False

    memory = inputs.copy() + [0] * 1000

    while not exit_program:
        instruction = int(str(memory[instruction_pointer])[-2:].lstrip("0"))
        mode = str(memory[instruction_pointer])[:-2].rjust(3, '0')

        if instruction == HALT.opcode:
            exit_program = True
        elif instruction == ADD.opcode:
            memory[resolve_parameter_address(memory, instruction_pointer + 3, mode[-3], relative_base)] = \
                resolve_parameter_value(memory, instruction_pointer + 1, mode[-1],  relative_base) + \
                resolve_parameter_value(memory, instruction_pointer + 2, mode[-2], relative_base)
            instruction_pointer += advance_instruction_pointer(ADD)
        elif instruction == MULTIPLY.opcode:
            memory[resolve_parameter_address(memory, instruction_pointer + 3, mode[-3], relative_base)] = \
                resolve_parameter_value(memory, instruction_pointer + 1, mode[-1], relative_base) * \
                resolve_parameter_value(memory, instruction_pointer + 2, mode[-2], relative_base)
            instruction_pointer += advance_instruction_pointer(MULTIPLY)
        elif instruction == INPUT.opcode:
            memory[resolve_parameter_address(memory, instruction_pointer + 1, mode[-1], relative_base)] = \
                input_queue.get()
            instruction_pointer += advance_instruction_pointer(INPUT)
        elif instruction == OUTPUT.opcode:
            output_queue.put(resolve_parameter_value(memory, instruction_pointer + 1, mode[-1], relative_base))
            instruction_pointer += advance_instruction_pointer(OUTPUT)
        elif instruction == JUMP_IF_TRUE.opcode:
            if resolve_parameter_value(memory, instruction_pointer + 1, mode[-1], relative_base) != 0:
                instruction_pointer = resolve_parameter_value(memory, instruction_pointer + 2, mode[-2], relative_base)
            else:
                instruction_pointer += advance_instruction_pointer(JUMP_IF_TRUE)
        elif instruction == JUMP_IF_FALSE.opcode:
            if resolve_parameter_value(memory, instruction_pointer + 1, mode[-1], relative_base) == 0:
                instruction_pointer = resolve_parameter_value(memory, instruction_pointer + 2, mode[-2], relative_base)
            else:
                instruction_pointer += advance_instruction_pointer(JUMP_IF_FALSE)
        elif instruction == LESS_THAN.opcode:
            if resolve_parameter_value(memory, instruction_pointer + 1, mode[-1], relative_base) < \
                    resolve_parameter_value(memory, instruction_pointer + 2, mode[-2], relative_base):
                memory[resolve_parameter_address(memory, instruction_pointer + 3, mode[-3], relative_base)] = 1
            else:
                memory[resolve_parameter_address(memory, instruction_pointer + 3, mode[-3], relative_base)] = 0
            instruction_pointer += advance_instruction_pointer(LESS_THAN)
        elif instruction == EQUALS.opcode:
            if resolve_parameter_value(memory, instruction_pointer + 1, mode[-1], relative_base) == \
                    resolve_parameter_value(memory, instruction_pointer + 2, mode[-2], relative_base):
                memory[resolve_parameter_address(memory, instruction_pointer + 3, mode[-3], relative_base)] = 1
            else:
                memory[resolve_parameter_address(memory, instruction_pointer + 3, mode[-3], relative_base)] = 0
            instruction_pointer += advance_instruction_pointer(EQUALS)
        elif instruction == REL_BASE_OFFSET.opcode:
            relative_base += resolve_parameter_value(memory, instruction_pointer + 1, mode[-1], relative_base)
            instruction_pointer += advance_instruction_pointer(REL_BASE_OFFSET)
        else:
            print("Hit unknown opcode " + str(instruction))
            exit_program = True

    return output_queue

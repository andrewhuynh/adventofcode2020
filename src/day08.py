import re
import copy


def get_acc_before_loop(x):
    accumulator = 0
    with open(x, "r") as f:
        boot_code = [instruction.strip().split(" ") for instruction in f.readlines()]
        executed_instruction_indexes = []
        i = 0
        while i not in executed_instruction_indexes and i < len(boot_code):
            executed_instruction_indexes.append(i)
            if boot_code[i][0] == "acc":
                operator = boot_code[i][1][0]
                operand = boot_code[i][1][1:]
                if operator == "+":
                    accumulator += int(operand)
                elif operator == "-":
                    accumulator -= int(operand)
                i += 1
            elif boot_code[i][0] == "jmp":
                operator = boot_code[i][1][0]
                operand = boot_code[i][1][1:]
                if operator == "+":
                    i += int(operand)
                elif operator == "-":
                    i -= int(operand)
            elif boot_code[i][0] == "nop":
                i += 1
        # print(executed_instruction_indexes)
    return accumulator


def get_acc_and_check(boot_code):
    # run through commands and return accumulator if finite
    accumulator = 0
    is_finite_loop = False
    executed_instruction_indexes = []
    i = 0
    while i not in executed_instruction_indexes and i < len(boot_code) and not is_finite_loop:
        executed_instruction_indexes.append(i)
        if boot_code[i][0] == "acc":
            operator = boot_code[i][1][0]
            operand = boot_code[i][1][1:]
            if operator == "+":
                accumulator += int(operand)
            elif operator == "-":
                accumulator -= int(operand)
            i += 1
        elif boot_code[i][0] == "jmp":
            operator = boot_code[i][1][0]
            operand = boot_code[i][1][1:]
            if operator == "+":
                i += int(operand)
            elif operator == "-":
                i -= int(operand)
        elif boot_code[i][0] == "nop":
            i += 1
        if i == len(boot_code):
            is_finite_loop = True
    return [accumulator, is_finite_loop]


def get_acc_for_finite_program(x):
    accumulator = 0
    with open(x, "r") as f:
        original_boot_code = [instruction.strip().split(" ") for instruction in f.readlines()]
        check_original_results = get_acc_and_check(original_boot_code)
        accumulator = check_original_results[0]
        fix_is_found = check_original_results[1]
        # iterator to find next nop or jmp
        i = 0
        while not fix_is_found and i < len(original_boot_code):
            # logic to flip next nop or jmp
            flipped_boot_code = copy.deepcopy(original_boot_code)
            if original_boot_code[i][0] == "acc":
                None
            elif original_boot_code[i][0] == "nop":
                flipped_boot_code[i][0] = "jmp"
            elif original_boot_code[i][0] == "jmp":
                flipped_boot_code[i][0] = "nop"
            check_results = get_acc_and_check(flipped_boot_code)
            accumulator = check_results[0]
            fix_is_found = check_results[1]
            i += 1
        if i == len(original_boot_code) and not fix_is_found:
            return 0
    return accumulator

# def flip_and_check(x):
#     accumulator = 0
#     with open(x, "r") as f:
#         boot_code = [instruction.strip().split(" ") for instruction in f.readlines()]
#         done = False
#         i = 0
#         while not done and i < len(boot_code):
#             if i == len(boot_code) - 1:
#                 done = True
#             # flip ju
#         j = 0
#         while not done and j < len(boot_code):
#     return accumulator

# def get_acc_after_fix(x):
#     accumulator = 0
#     with open(x, "r") as f:
#         boot_code = [instruction.strip().split(" ") for instruction in f.readlines()]
#         boot_code_redux = copy.deepcopy(boot_code)
#         executed_instruction_indexes = []
#         i = 0
#         while i not in executed_instruction_indexes and i < len(boot_code):
#             executed_instruction_indexes.append(i)
#             if boot_code[i][0] == "acc":
#                 boot_code_redux[i][1] = str(i + 1)
#                 i += 1
#             elif boot_code[i][0] == "jmp":
#                 operator = boot_code[i][1][0]
#                 operand = boot_code[i][1][1:]
#                 if operator == "+":
#                     boot_code_redux[i][1] = str(i + int(operand))
#                 elif operator == "-":
#                     boot_code_redux[i][1] = str(i - int(operand))
#                 i += 1
#             elif boot_code[i][0] == "nop":
#                 boot_code_redux[i][1] = str(i + 1)
#                 i += 1
#         destinations = []
#         k = 0
#         while k < len(boot_code_redux):
#             sanity_check = boot_code_redux[k][1]
#             if boot_code_redux[k][1] in destinations:
#                 # print(boot_code_redux[k][1])
#                 print("%s at %s is already in destinations!" % (boot_code_redux[k][1], k))
#             else:
#                 destinations.append(boot_code_redux[k][1])
#             k += 1
#         j = 0
#         # while j < len(boot_code_redux):
#         #     print(str(boot_code_redux[j])) # + " " + str(boot_code[j]))
#         #     j += 1
#         # for instruction in boot_code_redux:
#         #     print(instruction)
#     return accumulator

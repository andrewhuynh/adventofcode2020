import re

def weird_arithmetic(x):
    # "2 + 3 * 4"
    # assumes no parentheses
    problem = x.replace(" ", "")
    # stack = []
    first_number = problem[0]
    i = 1
    while i < len(problem) and "0" <= problem[i] <= "9":
        first_number += problem[i]
        i += 1
    answer = int(first_number)
    while i < len(problem):
        if problem[i] in "*":
            multiplicand = problem[i+1]
            i += 2
            while i < len(problem) and "0" <= problem[i] <= "9":
                multiplicand += problem[i]
                i += 1
            answer *= int(multiplicand)
        elif problem[i] == "+":
            addend = problem[i+1]
            i += 2
            while i < len(problem) and "0" <= problem[i] <= "9":
                addend += problem[i]
                i += 1
            answer += int(addend)
    # print(stack)
    return answer


def handle_parentheses(x):
    # 4 + ((2 * 3) + (4 * 5))
    problem = x.replace(" ", "")
    # problem = x

    while "(" in problem: # repeat until parentheses are gone
        stack = []
        for character in problem:
            if character != ")":
                stack.append(character)
            elif character == ")":
                # print(stack)
                temp = ""
                top = stack.pop()
                while top != "(":
                    temp = top + temp
                    top = stack.pop()
                # print(temp)
                # print(weird_arithmetic(temp))
                # print(temp)
                # print(problem)
                old = "(" + temp + ")"
                new = str(weird_arithmetic(temp))
                problem = problem.replace(old, new)
                # print(problem)
                break

    # print(problem)
    return problem


def solve_it(x):
    flat = handle_parentheses(x)
    return weird_arithmetic(flat)


def operation_order(x):
    with open(x, "r") as f:
        solutions = [solve_it(problem.strip("\n")) for problem in f.readlines()]
    return sum(solutions)


def add_parentheses_for_addition(x):
    # "10 + 20 * 30 + 40 * 50 + 60"
    # assumes no parentheses
    problem = x.replace(" ", "")
    additions = re.findall("[0-9]+\+[0-9]+", problem)
    for addition in additions:
        problem = problem.replace(addition, "("+addition+")")
    # print(problem)
    return problem


def add_parentheses_for_addition_complex(x):
    # (2*3)+(4*5)
    problem = x.replace(" ", "")
    # print(problem)
    i = 0
    additions = []
    while i < len(problem):
        if problem[i] == "+":
            # print(problem[i])

            # go left
            addition_start = i - 1
            if "0" <= problem[addition_start] <= "9":
                while addition_start - 1 >= 0 and "0" <= problem[addition_start - 1] <= "9":
                    addition_start -= 1
            elif problem[addition_start] == ")":
                left_stack = [problem[addition_start]]
                addition_start -= 1
                while addition_start > 0 and len(left_stack) > 0:
                    if problem[addition_start] == ")":
                        left_stack.append(problem[addition_start])
                        addition_start -= 1
                    elif problem[addition_start] == "(":
                        left_stack.pop()
                        if len(left_stack) > 0:
                            addition_start -= 1
                    # elif "0" <= problem[addition_start] <= "9":
                    else:
                        addition_start -= 1
            # print(addition_start)

            # go right
            addition_end = i + 1
            if "0" <= problem[addition_end] <= "9":
                while addition_end + 1 < len(problem) and "0" <= problem[addition_end + 1] <= "9":
                    addition_end += 1
            elif problem[addition_end] == "(":
                right_stack = [problem[addition_end]]
                addition_end += 1
                while addition_end <= len(problem) and len(right_stack) > 0:
                    if problem[addition_end] == "(":
                        right_stack.append(problem[addition_end])
                        addition_end += 1
                    elif problem[addition_end] == ")":
                        right_stack.pop()
                        if len(right_stack) > 0:
                            addition_end += 1
                    # elif "0" <= problem[addition_end] <= "9":
                    else:
                        addition_end += 1
            # print(addition_end)
            # print()
            addition_start_to_end = problem[addition_start:addition_end+1]
            additions.append(addition_start_to_end)
            # problem = problem.replace(addition_start_to_end, "(" + addition_start_to_end + ")")
            problem = problem[:addition_start] + "(" + addition_start_to_end + ")" + problem[addition_end + 1:]
            i += 2
        i += 1
    # for addition in additions:
    #     problem = problem.replace(addition, "(" + addition + ")")
    # print(problem)
    return problem


def solve_it_part_two(x):
    add_parentheses = add_parentheses_for_addition_complex(x)
    flat = handle_parentheses(add_parentheses)
    return weird_arithmetic(flat)


def operation_order_part_two(x):
    with open(x, "r") as f:
        solutions = [solve_it_part_two(problem.strip("\n")) for problem in f.readlines()]
        # print(solutions)
    return sum(solutions)

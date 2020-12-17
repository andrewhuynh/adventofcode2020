

def fun(x):
    return x + 1


def report_repair_two(x):
    f = open(x)
    expenses_raw = f.readlines()
    f.close()
    expenses = [int(i) for i in expenses_raw]
    # find the two numbers that add up to 2020
    i = 0
    while i < len(expenses):
        b = 2020-expenses[i]
        if expenses.count(b) > 0:
            return expenses[i] * expenses[expenses.index(b)]
        i = i + 1
    return 0


def report_repair_three(x):
    f = open(x)
    expenses_raw = f.readlines()
    f.close()
    expenses = [int(i) for i in expenses_raw]
    # find the three  numbers that add up to 2020
    i = 0
    while i < len(expenses):
        j = i + 1
        a = expenses[i]
        sum_b_c = 2020 - a
        while j < len(expenses):
            b = expenses[j]
            c = sum_b_c - b
            if expenses.count(c) > 0:
                return a * b * c
            j = j + 1
        i = i + 1
    return 0

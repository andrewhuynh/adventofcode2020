

def get_row(pass_number):
    row = 0
    i = 0
    row_length = 7
    while i < row_length:
        # print(pass_number[i])
        if pass_number[i] == "B":
            addend = 2 ** (row_length - 1 - i)
            # print("addend: %s" % addend)
            # print("i: %s" % i)
            row += addend
        i += 1
    return row


def get_column(pass_number):
    column = 0
    i = 7
    column_length = 3 + i
    while i < column_length:
        # print(pass_number[i])
        if pass_number[i] == "R":
            addend = 2 ** (column_length - 1 - i)
            # print("addend: %s" % addend)
            # print("i: %s" % i)
            column += addend
        i += 1
    return column


def get_seat_id(pass_number):
    row = get_row(pass_number)
    column = get_column(pass_number)
    seat_id = (row * 8) + column
    return seat_id


def get_highest_seat_id(x):
    f = open(x)
    boarding_passes_raw = f.readlines()
    f.close()
    highest_seat_id = get_seat_id(boarding_passes_raw[0])
    for boarding_pass in boarding_passes_raw:
        next_seat_id = get_seat_id(boarding_pass)
        if next_seat_id > highest_seat_id:
            highest_seat_id = next_seat_id
    return highest_seat_id


def get_missing_seat_id(x):
    f = open(x)
    seat_ids = [get_seat_id(boarding_pass) for boarding_pass in f.readlines()]
    seat_ids.sort()
    start = seat_ids[0]
    missing_seat_id = 0
    i = 0
    not_done = True
    while i < len(seat_ids) and not_done:
        if (i + start) not in seat_ids:
            not_done = False
            missing_seat_id = (i + start)
        i += 1
    f.close()

    return missing_seat_id

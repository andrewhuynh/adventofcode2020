

def scanning_error_rate(file):
    f = open(file)
    notes_raw = f.readlines()
    f.close()
    lines = [i.split() for i in notes_raw]
    print(lines)
    return 0


def scanning_error_rate_2(file):
    f = open(file)
    notes_raw = f.readlines()
    f.close()

    return 0

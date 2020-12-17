

def tree_encounters(file, x, y):
    f = open(file)
    lines = f.readlines()
    f.close()

    tree_count = 0
    base_width = len(lines[0])
    # print(base_width)
    height = len(lines)
    # print(height)
    slope_x = x
    slope_y = y
    # print(slope_x * height)
    # print(base_width)
    scale = int(slope_x * height / base_width)
    # print(scale)
    hill = [(scale + 3) * line.strip() for line in lines]
    # print(len(hill[0]))
    # # ignore the first line
    i = 1
    while i * slope_y < len(hill):
        # print(i)
        if hill[i * slope_y][i * slope_x] == "#":
            tree_count = tree_count + 1
        i = i + 1
    return tree_count


def multiply_tree_encounters(file):
    slope_1 = tree_encounters(file, 1, 1)
    print(slope_1)
    slope_2 = tree_encounters(file, 3, 1)
    print(slope_2)
    slope_3 = tree_encounters(file, 5, 1)
    print(slope_3)
    slope_4 = tree_encounters(file, 7, 1)
    print(slope_4)
    slope_5 = tree_encounters(file, 1, 2)
    print(slope_5)
    product = slope_1 * slope_2 * slope_3 * slope_4 * slope_5
    print(product)
    return product

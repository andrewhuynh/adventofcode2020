import re

def get_color_count(x):
    number_of_bag_colors_that_can_hold_at_least_one_shiny_gold_bag = 0
    bag_color = "shiny gold"
    with open(x, "r") as f:
        rules = [line.split(" bags contain ") for line in f.readlines()]
        bag_holders = set()
        for rule in rules:
            # rule[1] = rule[1].strip().strip(".").split(", ")
            if bag_color in rule[1]:
                bag_holders.add(rule[0])
            # print(rule)
        # print(bag_holders)
        next_level_bag_holders = set()
        for rule in rules:
            for color in bag_holders:
                if color in rule[1]:
                    next_level_bag_holders.add(rule[0])
        # print(next_level_bag_holders)

        # loop_count = 0
        while bag_holders != bag_holders.union(next_level_bag_holders):
            # loop_count += 1
            bag_holders = bag_holders.union(next_level_bag_holders)
            # print(bag_holders)
            new_level_bag_holders = set()
            for rule in rules:
                for color in next_level_bag_holders:
                    if color in rule[1]:
                        new_level_bag_holders.add(rule[0])
            next_level_bag_holders = new_level_bag_holders
            # print(bag_holders)
            # print(next_level_bag_holders)
        # print(loop_count)

        number_of_bag_colors_that_can_hold_at_least_one_shiny_gold_bag = len(bag_holders)
    return number_of_bag_colors_that_can_hold_at_least_one_shiny_gold_bag


def color_sum(color, rules_lookup):
    bag_content = rules_lookup[color][0]
    # print(bag_content)
    if bag_content == '0':
        return 0
    else:
        color_total = 0
        for content in rules_lookup[color]:
            # print(content)
            content_count = int(re.findall("^[0-9]+", content)[0])
            content_color = re.findall("[a-z]+\\s[a-z]+$", content)[0]
            color_total += content_count + content_count * color_sum(content_color, rules_lookup)
        return color_total


def get_number_of_bags_required(x):
    bag_color = "shiny gold"
    bags_required = 0
    with open(x, "r") as f:
        rules = [line.split(" bags contain ") for line in f.readlines()]
        rule_lookup = {}
        for rule in rules:
            rule_lookup[rule[0]] = rule[1].strip().strip(".").replace("no other bags", "0").replace(" bags", "")\
                .replace(" bag", "").split(", ")
        # print(rule_lookup)
        bags_required = color_sum(bag_color, rule_lookup)
    return bags_required
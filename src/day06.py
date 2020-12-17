

def groups_sum(x):
    count = 0
    with open(x, "r") as f:
        customs_forms = [form.replace("\n", "") for form in f.read().split("\n\n")]
        unique_forms = []
        for form in customs_forms:
            form_set = set()
            for character in form:
                form_set.add(character)
            unique_forms.append(form_set)
        # print(unique_forms)
        for form in unique_forms:
            # print(len(form))
            count += len(form)
    return count


def count_unanimous_yes(x):
    unanimous_yes = 0
    with open(x, "r") as f:
        customs_forms = [group.split("\n") for group in f.read().split("\n\n")]
        # print(customs_forms)
        for group in customs_forms:
            # find common characters in list elements
            first_person = group[0]
            # print(first_person)
            for character in first_person:
                # check if that character exists in each following person
                unanimous = True
                for person in group:
                    if character not in person:
                        # print("%s not in %s" % (character, person))
                        unanimous = False
                if unanimous:
                    unanimous_yes += 1

    return unanimous_yes

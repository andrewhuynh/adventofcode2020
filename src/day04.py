import re


def papers_please(file):
    f = open(file)
    passports_raw = f.read()
    f.close()
    passports = [i.replace("\n"," ") for i in passports_raw.split("\n\n")]
    # print(passports)
    valid_count = 0
    for entry in passports:
        # print(entry)
        fields = [field.split(":")[0] for field in entry.split()]
        if "byr" in fields and "iyr" in fields and "eyr" in fields and "hgt" in fields and "hcl" in fields and "ecl" in fields and "pid" in fields:
            valid_count += 1
    return valid_count


def stricter_papers_please(file):
    f = open(file)
    passports_raw = f.read()
    f.close()
    passports = [i.replace("\n"," ") for i in passports_raw.split("\n\n")]
    # print(passports)
    valid_count = 0
    for entry in passports:
        # print(entry)
        person = {}
        fields = [field.split(":") for field in entry.split()]
        for item in fields:
            person[item[0]] = item[1]
        if "byr" in person and "iyr" in person and "eyr" in person and "hgt" in person and "hcl" in person and "ecl" in person and "pid" in person:
            if 1920 <= int(person["byr"]) <= 2002 and 2010 <= int(person["iyr"]) <= 2020 <= int(person["eyr"]) <= 2030:
                if person["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    if re.search("^#[0-9a-f]{6}$", person["hcl"]):
                        # print("valid hcl: %s", person["hcl"])
                        if re.search("^[0-9]{9}$", person["pid"]):
                            # print("valid pid: %s" % person["pid"])
                            if (person["hgt"].endswith("cm") and 150 <= int(person["hgt"][:-2]) <= 193) or (person["hgt"].endswith("in") and 59 <= int(person["hgt"][:-2]) <= 76):
                                valid_count += 1
                            else:
                                # print("invalid height: %s" % person["hgt"])
                                None
                        else:
                            # print("invalid pid: %s" % person["pid"])
                            None

    return valid_count

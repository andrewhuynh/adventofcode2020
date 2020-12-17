

def sled_password_checker(x):
    f = open(x)
    passwords_raw = f.readlines()
    f.close()

    count_valid_passwords = 0
    for line in passwords_raw:
        entry = line.split(": ")
        policy = entry[0]
        policy_lower = int(policy.split("-")[0])
        policy_upper = int(policy.split("-")[1].split(" ")[0])
        policy_letter = policy.split(" ")[1]
        password = entry[1]
        if policy_lower <= password.count(policy_letter) <= policy_upper:
            count_valid_passwords = count_valid_passwords + 1

    return count_valid_passwords


def toboggan_password_checker(x):
    f = open(x)
    passwords_raw = f.readlines()
    f.close()

    count_valid_passwords = 0
    for line in passwords_raw:
        entry = line.split(": ")
        policy = entry[0]
        policy_lower = int(policy.split("-")[0])
        policy_upper = int(policy.split("-")[1].split(" ")[0])
        policy_letter = policy.split(" ")[1]
        password = entry[1]
        if (password[policy_lower - 1] == policy_letter) ^ (password[policy_upper - 1] == policy_letter):
            count_valid_passwords = count_valid_passwords + 1

    return count_valid_passwords

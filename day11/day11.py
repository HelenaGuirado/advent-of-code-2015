import string

INPUT = "hxbxwxba"
ALPHABET_LIST = list(string.ascii_lowercase)
NON_WANTED_NUMBERS = [ALPHABET_LIST.index("i"), ALPHABET_LIST.index("o"), ALPHABET_LIST.index("l")]

def check_rule_1(input):
    for idx, number in enumerate(input[:-2]):
        if number + 1 == input[idx + 1] and number + 2 == input[idx + 2]:
            return True
    return False

def check_rule_2(input):
    return not any(x in input for x in NON_WANTED_NUMBERS)

def check_rule_3(input):
    found = 0
    idx = 0
    while idx < 7:
        if input[idx] == input[idx + 1]:
            found += 1
            idx += 1
        idx += 1
    return found == 2

def is_good_password(input):
    return check_rule_1(input) and check_rule_2(input) and check_rule_3(input)

def find_password(number_input):
    password_found = False
    while not password_found:
        idx = len(number_input) - 1
        new_password = False
        while not new_password:
            if number_input[idx] == 25:
                number_input[idx] = 0
                idx -= 1
            elif number_input[idx] + 1 in NON_WANTED_NUMBERS:
                number_input[idx] += 2
                new_password = True
            else:
                number_input[idx] += 1
                new_password = True
        password_found = is_good_password(number_input)
    return number_input

part_1_number_input = [ALPHABET_LIST.index(INPUT[idx]) for idx in range(len(INPUT))]
part_1_number_result = find_password(part_1_number_input)
part_1_result = "".join([ALPHABET_LIST[part_1_number_result[idx]] for idx in range(len(part_1_number_result))])

part_2_number_result = find_password(part_1_number_result)
part_2_result = "".join([ALPHABET_LIST[part_2_number_result[idx]] for idx in range(len(part_2_number_result))])

print("Day 11 part 1 result: " + part_1_result)
print("Day 11 part 2 result: " + part_2_result)
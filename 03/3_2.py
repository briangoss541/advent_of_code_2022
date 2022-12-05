import string

test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

with open('input.txt') as in_file:
    input_string = in_file.read()

priority_dict = {k: v for k, v in zip(string.ascii_lowercase, range(1, 27))}
priority_dict.update({k: v for k, v in zip(string.ascii_uppercase, range(27, 53))})

priority_sum = 0
string_target = input_string
ruck_list = string_target.split('\n')
for ruck_group_pointer in range(0, len(ruck_list) - 3, 3):

    first_ruck = ruck_list[ruck_group_pointer]
    second_ruck = ruck_list[ruck_group_pointer + 1]
    third_ruck = ruck_list[ruck_group_pointer + 2]

    first_set = {x for x in first_ruck}
    second_set = {x for x in second_ruck}
    third_set = {x for x in third_ruck}

    shared_item = (first_set & second_set & third_set).pop()

    priority_sum += priority_dict[shared_item]

print(priority_sum)

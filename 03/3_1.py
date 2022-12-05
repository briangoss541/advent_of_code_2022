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
for ruck_row in input_string.split('\n'):

    if ruck_row == '':
        continue

    first_ruck = ruck_row[:int(len(ruck_row)/2)]
    second_ruck = ruck_row[int(len(ruck_row)/2):]

    first_set = {x for x in first_ruck}
    second_set = {x for x in second_ruck}

    shared_item = (first_set & second_set).pop()

    priority_sum += priority_dict[shared_item]

print(priority_sum)

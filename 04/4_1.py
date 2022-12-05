test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

with open('input.txt') as in_file:
    input_string = in_file.read()

target_input = input_string

overlap_counter = 0
for row in target_input.split('\n'):

    if row == '':
        continue

    first_elf, second_elf = row.split(',')

    first_range_start, first_range_end = first_elf.split('-')
    second_range_start, second_range_end = second_elf.split('-')

    first_set = {x for x in range(int(first_range_start), int(first_range_end) + 1)}
    second_set = {x for x in range(int(second_range_start), int(second_range_end) + 1)}

    if len(first_set - second_set) == 0 or len(second_set - first_set) == 0:
        overlap_counter += 1

print(overlap_counter)

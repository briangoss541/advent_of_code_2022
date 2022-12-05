from collections import defaultdict

test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

with open('input.txt') as in_file:
    input_string = in_file.read()

# stack_chart_width = 12
stack_chart_width = 36

crate_window = 3

crate_process_flag = True
crate_tracker = defaultdict(list)

target_input = input_string

for row in target_input.split('\n'):

    if crate_process_flag is True:

        if row == '':
            crate_process_flag = False
            continue

        # Process thy crates
        row_crates = [row[i:i + crate_window] for i in range(0, len(row), crate_window + 1)]
        print(row_crates)

        for crate_index, crate_string in enumerate(row_crates):

            create_string = crate_string.strip('[]').strip()

            if create_string.isalpha() is True:

                crate_tracker[crate_index + 1].insert(0, create_string)

    else:

        if row == '':
            continue

        move_string, direction_string = row.split('from')
        move_amount = int(move_string.split(' ')[1])
        direction_list = direction_string.strip().split(' ')
        direction_list = [int(x) for x in direction_list if not x.isalpha()]

        moving_crates = list()
        for _ in range(move_amount):
            moving_crate = crate_tracker[direction_list[0]].pop()
            moving_crates.insert(0, moving_crate)

        crate_tracker[direction_list[1]] += moving_crates

print(crate_tracker)

for stack in sorted(crate_tracker.keys()):
    print(crate_tracker[stack][-1])

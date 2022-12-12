test_string = """noop
addx 3
addx -5"""

test_string = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

with open('input.txt') as in_file:
    input_string = in_file.read()

x_register = 1
cycle_num = 1

cycle_log = dict({cycle_num: x_register})

# for program_line in test_string.splitlines():
for program_line in input_string.splitlines():

    if 'addx' in program_line:

        _, value = program_line.strip().split(' ')
        value = int(value)

        cycle_num += 1
        cycle_log.update({cycle_num: x_register})
        cycle_num += 1
        x_register += value
        cycle_log.update({cycle_num: x_register})

    elif 'noop' in program_line:

        cycle_num += 1
        cycle_log.update({cycle_num: x_register})

crt_screen = ['.'] * 240

for crt_cycle in range(0, 240):

    row_offset = 0
    for row_boundary in reversed([40, 80, 120, 160, 200, 240]):
        if crt_cycle >= row_boundary:
            row_offset = row_boundary
            break

    sprite_location = cycle_log[crt_cycle + 1]

    sprite_coverage = [sprite_location - 1, sprite_location, sprite_location + 1]

    if crt_cycle - row_offset in sprite_coverage:
        crt_screen[crt_cycle] = '#'

for start_row, end_row in [(0, 40), (40, 80), (80, 120), (120, 160), (160, 200), (200, 240)]:
    print(''.join(crt_screen[start_row:end_row]))

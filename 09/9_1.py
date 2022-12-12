test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

with open('input.txt') as in_file:
    input_string = in_file.read()

h_pos = (0, 0)
t_pos = (0, 0)

h_coord_list = list()
visited_coords = {t_pos}

# for row in test_input.splitlines():
for row in input_string.splitlines():

    move_direction, move_count = row.split(' ')
    move_count = int(move_count)

    for _ in range(move_count):

        if move_direction == 'U':
            h_pos = (h_pos[0], h_pos[1] + 1)
        elif move_direction == 'R':
            h_pos = (h_pos[0] + 1, h_pos[1])
        elif move_direction == 'D':
            h_pos = (h_pos[0], h_pos[1] - 1)
        elif move_direction == 'L':
            h_pos = (h_pos[0] - 1, h_pos[1])

        if abs(h_pos[0] - t_pos[0]) == 2 or abs(h_pos[1] - t_pos[1]) == 2:
            t_pos = h_coord_list[-1]
            visited_coords.add(t_pos)

        h_coord_list.append(h_pos)

print(len(visited_coords))
# 6213 too high

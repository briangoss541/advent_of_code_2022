# test_input = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""

test_input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

with open('input.txt') as in_file:
    input_string = in_file.read()

# h_pos = (0, 0)
pos_list = [[0, 0] for _ in range(10)]
# prev_coord_list = [(0, 0) for _ in range(10)]
visited_coords = set()

# for row in test_input.splitlines():
for row in input_string.splitlines():

    move_direction, move_count = row.split(' ')
    move_count = int(move_count)

    sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)

    for _ in range(move_count):

        h_pos = pos_list[0]

        if move_direction == 'U':
            h_pos = [h_pos[0], h_pos[1] + 1]
        elif move_direction == 'R':
            h_pos = [h_pos[0] + 1, h_pos[1]]
        elif move_direction == 'D':
            h_pos = [h_pos[0], h_pos[1] - 1]
        elif move_direction == 'L':
            h_pos = [h_pos[0] - 1, h_pos[1]]

        pos_list[0] = h_pos

        # for i in range(1, 10):
        #     dist = rope[i-1] - rope[i]
        #     if abs(dist) >= 2:
        #         rope[i] += sign(dist)
        #         seen[i].add(rope[i])

        for knot_num in range(1, 10):

            preceding_knot = pos_list[knot_num - 1]
            current_knot = pos_list[knot_num]

            if (current_knot[0] - preceding_knot[0]) == 0 or (current_knot[1] - preceding_knot[1]) == 0:
                if abs(current_knot[0] - preceding_knot[0]) >= 2:
                    current_knot[0] -= sign(current_knot[0] - preceding_knot[0])
                if abs(current_knot[1] - preceding_knot[1]) >= 2:
                    current_knot[1] -= sign(current_knot[1] - preceding_knot[1])
            elif (abs(current_knot[0] - preceding_knot[0]), abs(current_knot[1] - preceding_knot[1])) != (1, 1):
                current_knot[0] -= sign(current_knot[0] - preceding_knot[0])
                current_knot[1] -= sign(current_knot[1] - preceding_knot[1])

            visited_coords.add(tuple(pos_list[-1]))

print(len(visited_coords))
# 4856 too high
# 2687 too high
# 2685 too high

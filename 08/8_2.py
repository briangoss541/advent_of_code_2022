import numpy

test_input = """30373
25512
65332
33549
35390"""

with open('input.txt') as in_file:
    input_string = in_file.read()

height_grid = dict()
for row_index, row in enumerate(input_string.splitlines()):
    for col_index, tree_height in enumerate(row):
        height_grid.update({
            (col_index, row_index): int(tree_height)
        })

max_x = max([x for x, y in height_grid.keys()])
max_y = max([y for x, y in height_grid.keys()])

top_scenic_score = 0
for start_x, start_y in height_grid.keys():

    start_tree_height = height_grid[(start_x, start_y)]
    scenic_score_list = list()

    scenic_score = 0
    for check_x in range(start_x + 1, max_x + 1):  # Right
        scenic_score += 1
        if height_grid[(check_x, start_y)] >= start_tree_height:
            break
    scenic_score_list.append(scenic_score)

    scenic_score = 0
    for check_x in range(start_x - 1, -1, -1):  # Left
        scenic_score += 1
        if height_grid[(check_x, start_y)] >= start_tree_height:
            break
    scenic_score_list.append(scenic_score)

    scenic_score = 0
    for check_y in range(start_y + 1, max_y + 1):  # Down
        scenic_score += 1
        if height_grid[(check_y, start_x)] >= start_tree_height:
            break
    scenic_score_list.append(scenic_score)

    scenic_score = 0
    for check_y in range(start_y - 1, -1, -1):  # Up
        scenic_score += 1
        if height_grid[(check_y, start_x)] >= start_tree_height:
            break
    scenic_score_list.append(scenic_score)

    total_scenic = numpy.prod(scenic_score_list)
    if total_scenic > top_scenic_score:
        top_scenic_score = total_scenic

print(top_scenic_score)

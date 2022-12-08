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

visible_trees = set()
for check_y in range(max_y + 1):

    tallest_preceding_tree = -1
    for check_x in range(max_x + 1):
        if height_grid[(check_x, check_y)] > tallest_preceding_tree:
            visible_trees.add((check_x, check_y))
            tallest_preceding_tree = height_grid[(check_x, check_y)]

    tallest_preceding_tree = -1
    for check_x in range(max_x, -1, -1):
        if height_grid[(check_x, check_y)] > tallest_preceding_tree:
            visible_trees.add((check_x, check_y))
            tallest_preceding_tree = height_grid[(check_x, check_y)]

for check_x in range(max_x + 1):

    tallest_preceding_tree = -1
    for check_y in range(max_y + 1):
        if height_grid[(check_x, check_y)] > tallest_preceding_tree:
            visible_trees.add((check_x, check_y))
            tallest_preceding_tree = height_grid[(check_x, check_y)]

    tallest_preceding_tree = -1
    for check_y in range(max_y, -1, -1):
        if height_grid[(check_x, check_y)] > tallest_preceding_tree:
            visible_trees.add((check_x, check_y))
            tallest_preceding_tree = height_grid[(check_x, check_y)]

print(visible_trees)
print(len(visible_trees))

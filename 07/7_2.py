from collections import defaultdict

test_string = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

with open('input.txt') as in_file:
    input_string = in_file.read()

data_dict = defaultdict(list)
directory_path = str()
directory_set = set()

for line in input_string.splitlines():

    if line[0] == '$':  # Command

        if 'cd' in line:

            move_data = line[5:].strip()

            if move_data == '..':
                directory_path = '-'.join(directory_path.split('-')[:-1])
                continue

            directory_path += f"-{move_data}"
            directory_set.add(directory_path)

    else:

        first_element, second_element = line.split(' ')

        try:
            file_size = int(first_element)
        except ValueError:
            continue

        data_dict[directory_path].append({'name': second_element.strip(),
                                          'size': file_size})

print(data_dict)

def dir_count(input_path):
    size_counter = 0

    for check_dir_path in data_dict.keys():

        if input_path in check_dir_path:

            for file_data in data_dict[check_dir_path]:
                size_counter += file_data['size']

    return size_counter


filesystem_size = 70000000
target_unused = 30000000
current_unused = filesystem_size - dir_count('-/')
target_dir_size = target_unused - current_unused

best_size = target_unused

for dir_path in directory_set:

    dir_size = dir_count(dir_path)

    if dir_size > target_dir_size and dir_size < best_size:
        best_size = dir_size

print(best_size)

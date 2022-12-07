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

size_limit = 100000

filter_dir_sum = 0

for dir_path in directory_set:

    size_counter = 0

    for check_dir_path in data_dict.keys():

        if dir_path in check_dir_path:

            for file_data in data_dict[check_dir_path]:
                size_counter += file_data['size']

    if size_counter <= size_limit:
        filter_dir_sum += size_counter

print(filter_dir_sum)

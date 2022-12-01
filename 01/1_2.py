from collections import defaultdict

test_string = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

with open('input.txt') as in_file:
    input_string = in_file.read()

elf_num = 0
elf_dict = defaultdict(int)
for line in input_string.split('\n'):

    if line == '':
        elf_num += 1
    else:
        calories = int(line)
        elf_dict[elf_num] += calories

print(sum(sorted(elf_dict.values(), reverse=True)[0:3]))

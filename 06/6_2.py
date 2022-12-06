test_string = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

with open('input.txt') as in_file:
    input_string = in_file.read()

for char_index, string_char in enumerate(input_string):

    # Check if we're long enough
    if char_index < 13:
        continue

    test_set = set()
    for x in range(-13, 1):
        test_set.add(input_string[char_index + x])

    if len(test_set) == 14:
        print(f'Start of packet at {char_index + 1}')
        break

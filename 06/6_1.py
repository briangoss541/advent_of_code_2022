test_string = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

with open('input.txt') as in_file:
    input_string = in_file.read()

for char_index, string_char in enumerate(input_string):

    # Check if we're long enough
    if char_index < 3:
        continue

    test_set = {input_string[char_index - 3],
                input_string[char_index - 2],
                input_string[char_index - 1],
                input_string[char_index]}

    if len(test_set) == 4:
        print(f'Start of packet at {char_index + 1}')
        break

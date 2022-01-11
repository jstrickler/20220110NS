file_path = "DATA/mary.txt"

mary_in = open(file_path, "r")
# read data here ...
mary_in.close()

with open(file_path) as mary_in:
    for raw_line in mary_in:  # repeatedly call mary_in.readline()
        line = raw_line.rstrip()  # remove ' ' \t \n \r
        print(line)
print('-' * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()
    print("raw:")
    print(repr(contents))
    print("normal:")
    print(contents)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print('-' * 60)

with open('numbers.txt') as numbers_in:
    all_numbers_raw = numbers_in.read().splitlines()
    print(all_numbers_raw)
    all_numbers = [int(n) for n in all_numbers_raw]
    print(all_numbers)
print('-' * 60)


target = 's'
count = 0
with open('DATA/words.txt') as words_in:
    for word in words_in:
        if word.startswith(target):
            count += 1
print(f"{count} words start with '{target}'\n")

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:  # delete contents if existing
    for fruit in fruits:
        fruits_out.write(fruit + '\n')



target = 'x'
target_file = f"{target}_words.txt"
with open('DATA/words.txt') as words_in:
    with open(target_file, 'w') as target_out:
        for word in words_in:
            if word.startswith(target):
                target_out.write(word)









import re


file = open("day-03/inputs/part_1.txt", 'r')
file_contents = file.read()


numbers = [match for match in re.finditer("\d+", file_contents)]
symbols = [match for match in re.finditer("[^.0-9\n]", file_contents)]

N = file_contents.index('\n') + 1
adjacent_offsets = [
    -N-1, -N-0, -N+1,
      -1,   -0,   +1,
    +N-1, +N-0, +N+1,
]

adding_num_set = set()


for sym in symbols:
    sym_pos = sym.span()[0]

    for offset in adjacent_offsets:
        p = sym_pos + offset
        if p < 0 or p > len(file_contents):
            continue

        for num in numbers:
            if p in range(num.span()[0], num.span()[1]):
                adding_num_set.add(num)


sum_nums = 0

for num_match in adding_num_set:
    sum_nums += int(num_match.group())

print(sum_nums)

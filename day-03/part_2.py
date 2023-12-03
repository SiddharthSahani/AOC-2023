
import re


file = open("day-03/inputs/part_2.txt", 'r')
file_contents = file.read()


numbers = [match for match in re.finditer("\d+", file_contents)]
symbols = [match for match in re.finditer("[^.0-9\n]", file_contents)]

N = file_contents.index('\n') + 1
adjacent_offsets = [
    -N-1, -N-0, -N+1,
      -1,   -0,   +1,
    +N-1, +N-0, +N+1,
]


gears_map = {}

for sym in symbols:
    gears_map[sym] = set()
    sym_pos = sym.span()[0]
    
    for offset in adjacent_offsets:
        p = sym_pos + offset
        if p < 0 or p > len(file_contents):
            continue

        for num in numbers:
            if p in range(num.span()[0], num.span()[1]):
                gears_map[sym].add(num)


sum_gears = 0
for sym in symbols:
    l = list(gears_map[sym])
    if len(l) == 2:
        sum_gears += int(l[0].group()) * int(l[1].group())

print(sum_gears)

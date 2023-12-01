
file = open("day-01/inputs/part_1.txt", 'r')
file_contents = file.read()


sum_vals = 0

for line in file_contents.splitlines():
    first = -1
    last = -1

    for char in line:
        if char.isdigit():
            first = int(char)
            break

    for char in reversed(line):
        if char.isdigit():
            last = int(char)
            break

    num = first * 10 + last
    sum_vals += num


print(sum_vals)

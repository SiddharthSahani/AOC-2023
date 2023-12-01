
file = open("day-01/inputs/part_2.txt", 'r')
file_contents = file.read()


digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits_map = {
    digits[i]: f"{digits[i]}{i+1}{digits[i]}" for i in range(9)
}


for k, v in digits_map.items():
    file_contents = file_contents.replace(k, v)


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

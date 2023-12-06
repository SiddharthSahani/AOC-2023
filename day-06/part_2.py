
file = open("day-06/inputs/part_2.txt", 'r')
file_contents = file.read()

lines = file_contents.splitlines()


time = int(''.join(lines[0].split()[1:]))
distance = int(''.join(lines[1].split()[1:]))


num_ways = 0
for t in range(time):
    speed = t
    dist = (time - t) * speed
    if dist > distance:
        num_ways += 1
    else:
        if num_ways != 0:
            break


print(num_ways)

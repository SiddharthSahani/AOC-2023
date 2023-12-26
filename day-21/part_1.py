
file = open("day-21/inputs/part_1.txt", 'r')
file_contents = file.read()


lines = file_contents.splitlines()
nrows = len(lines)
ncols = len(lines[0])


start_pos = [None, None]
start_pos[0] = sum(i for i, line in enumerate(lines) if 'S' in line)
start_pos[1] = lines[start_pos[0]].index('S')
start_pos = tuple(start_pos)


queue = [start_pos]
for _ in range(64):
    print(_)
    for i in range(len(queue)):
        pos = queue.pop(0)
        for off in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            npos = (pos[0] + off[0], pos[1] + off[1])
            if npos not in queue and 0 <= npos[0] < nrows and 0 <= npos[1] < ncols and lines[npos[0]][npos[1]] != '#':
                queue.append(npos)

print(len(queue))

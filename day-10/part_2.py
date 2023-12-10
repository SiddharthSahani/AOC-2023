
file = open("day-10/inputs/part_2.txt")
file_contents = file.read()


lines = file_contents.splitlines()
N = len(lines)
grid = [[c for c in line] for line in lines]

start_position = [None, None]
start_position[0] = sum(i for i in range(N) if 'S' in grid[i])
start_position[1] = grid[start_position[0]].index('S')
start_position = tuple(start_position)


queue = [start_position]
visited = set(queue)
starting_pipes = set("|-JL7F")

while queue:
    pos = queue.pop(0)
    pipe = grid[pos[0]][pos[1]]

    if pos[0] > 0 and pipe in "S|JL" and grid[pos[0] - 1][pos[1]] in "|7F" and (pos[0] - 1, pos[1]) not in visited:
        visited.add((pos[0] - 1, pos[1]))
        queue.append((pos[0] - 1, pos[1]))
        if pipe == 'S':
            starting_pipes.intersection_update("|JL")
        
    if pos[0] < len(grid) - 1 and pipe in "S|7F" and grid[pos[0] + 1][pos[1]] in "|JL" and (pos[0] + 1, pos[1]) not in visited:
        visited.add((pos[0] + 1, pos[1]))
        queue.append((pos[0] + 1, pos[1]))
        if pipe == 'S':
            starting_pipes.intersection_update("|7F")

    if pos[1] > 0 and pipe in "S-J7" and grid[pos[0]][pos[1] - 1] in "-LF" and (pos[0], pos[1] - 1) not in visited:
        visited.add((pos[0], pos[1] - 1))
        queue.append((pos[0], pos[1] - 1))
        if pipe == 'S':
            starting_pipes.intersection_update("-J7")

    if pos[1] < len(grid[pos[0]]) - 1 and pipe in "S-LF" and grid[pos[0]][pos[1] + 1] in "-J7" and (pos[0], pos[1] + 1) not in visited:
        visited.add((pos[0], pos[1] + 1))
        queue.append((pos[0], pos[1] + 1))
        if pipe == 'S':
            starting_pipes.intersection_update("-LF")


s_value = next(iter(starting_pipes))

grid = [[(s_value if c == 'S' else c) for c in line] for line in lines]
grid = [[c if (x, y) in visited else '.' for y, c in enumerate(line)] for x, line in enumerate(grid)]

excluded = set()

for x, line in enumerate(grid):
    inside, flag = False, False
    for y, c in enumerate(line):
        match c:
            case '|':
                inside = not inside
            case 'L':
                flag = True
            case 'F':
                flag = False
            case '7' | 'J':
                inside = inside if c == ('J' if flag else '7') else not inside

        if not inside:
            excluded.add((x, y))

print(N*len(grid[0]) - len(excluded | visited))

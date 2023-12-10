
from math import ceil


file = open("day-10/inputs/part_1.txt")
file_contents = file.read()


lines = file_contents.splitlines()
N = len(lines)
grid = [[c for c in line] for line in lines]

start_position = [None, None]
start_position[0] = sum(i for i in range(N) if 'S' in grid[i])
start_position[1] = grid[start_position[0]].index('S')
start_position = tuple(start_position)


visited = set()
queue = [start_position]

while queue:
    pos = queue.pop(0)
    pipe = grid[pos[0]][pos[1]]

    if pos[0] > 0 and pipe in "S|JL" and grid[pos[0] - 1][pos[1]] in "|7F" and (pos[0] - 1, pos[1]) not in visited:
        visited.add((pos[0] - 1, pos[1]))
        queue.append((pos[0] - 1, pos[1]))
        
    if pos[0] < len(grid) - 1 and pipe in "S|7F" and grid[pos[0] + 1][pos[1]] in "|JL" and (pos[0] + 1, pos[1]) not in visited:
        visited.add((pos[0] + 1, pos[1]))
        queue.append((pos[0] + 1, pos[1]))

    if pos[1] > 0 and pipe in "S-J7" and grid[pos[0]][pos[1] - 1] in "-LF" and (pos[0], pos[1] - 1) not in visited:
        visited.add((pos[0], pos[1] - 1))
        queue.append((pos[0], pos[1] - 1))

    if pos[1] < len(grid[pos[0]]) - 1 and pipe in "S-LF" and grid[pos[0]][pos[1] + 1] in "-J7" and (pos[0], pos[1] + 1) not in visited:
        visited.add((pos[0], pos[1] + 1))
        queue.append((pos[0], pos[1] + 1))

print(ceil(len(visited) / 2))

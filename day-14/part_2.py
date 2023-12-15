
file = open("day-14/inputs/part_2.txt")
file_contents = file.read()


grid = [[c for c in line] for line in file_contents.splitlines()]
N = len(grid)


def roll(grid):
    for y in range(N):
        for x in range(N):
            if grid[x][y] == 'O':
                while grid[x-1][y] == '.' and x != 0:
                    grid[x][y] = '.'
                    grid[x-1][y] = 'O'
                    x = x-1
    return grid


def rotate(grid):
    new = [['' for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            new[y][N-x-1] = grid[x][y]
    return new


def cycle(grid):
    for _ in range(4):
        grid = roll(grid)
        grid = rotate(grid)
    return grid


seen = set(tuple(map(tuple, grid)))
states = [grid]

for i in range(1, 10**9):
    grid = cycle(grid)

    t_grid = tuple(map(tuple, grid))
    if t_grid in seen:
        break
    seen.add(t_grid)
    states.append(t_grid)


first_occ = states.index(t_grid)
cyclicity = i - first_occ
grid = states[(10**9 - first_occ) % cyclicity + first_occ]
print(sum(N-x for x, line in enumerate(grid) for y, char in enumerate(line) if char == 'O'))

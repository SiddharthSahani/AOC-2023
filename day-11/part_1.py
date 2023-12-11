
from itertools import combinations


file = open("day-11/inputs/part_1.txt")
file_contents = file.read()

grid = file_contents.splitlines()


empty_rows = [row_idx for row_idx, row in enumerate(grid) if '#' not in row]
empty_cols = [
    col_idx for col_idx in range(len(grid[0]))
    if all('#' not in row[col_idx] for row in grid)
]

galaxies = [
    (x, y)
    for x in range(len(grid)) for y in range(len(grid[0]))
    if grid[x][y] == '#'
]


sum_distances = 0

for g1, g2 in combinations(galaxies, r=2):
    min_x, max_x = (g1[0], g2[0]) if g1[0] < g2[0] else (g2[0], g1[0])
    min_y, max_y = (g1[1], g2[1]) if g1[1] < g2[1] else (g2[1], g1[1])
    dx = sum(1 if min_x < row <= max_x else 0 for row in empty_rows)
    dy = sum(1 if min_y < col <= max_y else 0 for col in empty_cols)
    sum_distances += max_x - min_x + max_y - min_y + dx + dy


print(sum_distances)

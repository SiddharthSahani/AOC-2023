
from heapq import heappush, heappop


file = open("day-17/inputs/part_1.txt", 'r')
file_contents = file.read()


grid = [[int(d) for d in line] for line in file_contents.splitlines()]
nrows = len(grid)
ncols = len(grid[0])


seen = set()
queue = [(0, (0, 0), '', 0)]

while True:
    hl, (x, y), d, n = heappop(queue)

    if x == nrows - 1 and y == ncols - 1:
        print(hl)
        break

    if ((x, y), d, n) in seen:
        continue

    seen.add(((x, y), d, n))
    
    if n < 3 and d:
        nx = x + ((1 if d == 'D' else -1) if d in 'UD' else 0)
        ny = y + ((1 if d == 'R' else -1) if d in 'LR' else 0)
        if 0 <= nx < nrows and 0 <= ny < ncols:
            heappush(queue, (hl + grid[nx][ny], (nx, ny), d, n + 1))

    if d in 'UD':
        if 0 <= y-1 < ncols: heappush(queue, (hl + grid[x][y-1], (x, y-1), 'L', 1))
        if 0 <= y+1 < ncols: heappush(queue, (hl + grid[x][y+1], (x, y+1), 'R', 1))
    if d in 'LR':
        if 0 <= x-1 < nrows: heappush(queue, (hl + grid[x-1][y], (x-1, y), 'U', 1))
        if 0 <= x+1 < nrows: heappush(queue, (hl + grid[x+1][y], (x+1, y), 'D', 1))

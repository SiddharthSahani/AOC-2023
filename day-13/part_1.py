
file = open("day-13/inputs/part_1.txt")
file_contents = file.read()


parts = file_contents.split('\n\n')


answer = 0

for part in parts:
    grid = [[c for c in line] for line in part.splitlines()]
    nrows = len(grid)
    ncols = len(grid[0])

    for row_idx in range(nrows-1):
        n_up = row_idx + 1
        n_down = nrows - n_up
        min_n = min(n_up, n_down)

        for i in range(min_n):
            if grid[row_idx - i] != grid[row_idx + i + 1]:
                break
        else:
            answer += 100 * n_up
            break

    else:
        for col_idx in range(ncols-1):
            n_left = col_idx + 1
            n_right = ncols - n_left
            min_n = min(n_left, n_right)

            for i in range(min_n):
                if any(line[col_idx - i] != line[col_idx + i + 1] for line in grid):
                    break
            else:
                answer += n_left

print(answer)


file = open("day-13/inputs/part_2.txt")
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

        diff = 0
        for i in range(min_n):
            diff += sum(c1 != c2 for c1, c2 in zip(grid[row_idx - i], grid[row_idx + i + 1]))

        if diff == 1:
            answer += 100 * n_up
            break

    else:
        for col_idx in range(ncols-1):
            n_left = col_idx + 1
            n_right = ncols - n_left
            min_n = min(n_left, n_right)

            diff = 0
            for i in range(min_n):
                diff += sum(line[col_idx - i] != line[col_idx + i + 1] for line in grid)

            if diff == 1:
                answer += n_left
                break

print(answer)

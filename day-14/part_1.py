
file = open("day-14/inputs/part_1.txt")
file_contents = file.read()


grid = [[c for c in line] for line in file_contents.splitlines()]
N = len(grid)


answer = 0

for y in range(N):
    for x in range(N):
        if grid[x][y] == 'O':
            while grid[x-1][y] == '.' and x != 0:
                grid[x][y] = '.'
                grid[x-1][y] = 'O'
                x = x-1
            answer += N - x

print(answer)

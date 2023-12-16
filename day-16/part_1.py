
file = open("day-16/inputs/part_1.txt", 'r')
file_contents = file.read()


lines = file_contents.splitlines()
nrows = len(lines)
ncols = len(lines[0])


energy_grid = [[0 for _ in range(ncols)] for _ in range(nrows)]
lights = [[0, -1, 'R']]
copy_grid = [["" for _ in range(ncols)] for _ in range(nrows)]

while any(lights):
    for i in range(len(lights)):
        light = lights[i]
        if not light:
            continue

        match light[2]:
            case 'U': light[0] -= 1
            case 'D': light[0] += 1
            case 'L': light[1] -= 1
            case 'R': light[1] += 1

        valid = 0 <= light[0] < ncols and 0 <= light[1] < nrows and light[2] not in copy_grid[light[0]][light[1]]
        if not valid:
            lights[i] = None
            continue

        energy_grid[light[0]][light[1]] = 1
        copy_grid[light[0]][light[1]] += light[2]

        char = lines[light[0]][light[1]]

        if char == '.':
            continue
        elif char == '|' and light[2] in "LR":
            light[2] = 'U'
            lights.append([light[0], light[1], 'D'])
        elif char == '-' and light[2] in "UD":
            light[2] = 'L'
            lights.append([light[0], light[1], 'R'])
        elif char == '/':
            match light[2]:
                case 'U': light[2] = 'R'
                case 'D': light[2] = 'L'
                case 'L': light[2] = 'D'
                case 'R': light[2] = 'U'
        elif char == '\\':
            match light[2]:
                case 'U': light[2] = 'L'
                case 'D': light[2] = 'R'
                case 'L': light[2] = 'U'
                case 'R': light[2] = 'D'

    invalids = [i for i, light in enumerate(lights) if not light]
    for i in reversed(invalids):
        lights.pop(i)

print(sum(sum(row) for row in energy_grid))

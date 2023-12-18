
file = open("day-18/inputs/part_1.txt", 'r')
file_contents = file.read()


lines = file_contents.splitlines()
instructions = [line.split() for line in lines]
instructions = [(instr[0], int(instr[1])) for instr in instructions]


polygon = [(0, 0)]
boundary_n = 0

for dir, n in instructions:
    boundary_n += n
    polygon.append((
        polygon[-1][0] + n * ((1 if dir == 'D' else -1) if dir in 'UD' else 0),
        polygon[-1][1] + n * ((1 if dir == 'R' else -1) if dir in 'LR' else 0)
    ))

area = sum(polygon[i][0] * (polygon[i-1][1] - polygon[i+1][1]) for i in range(len(polygon)-1))
area = abs(area) // 2

print(area + boundary_n // 2 + 1)

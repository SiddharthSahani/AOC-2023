
file = open("day-22/inputs/part_2.txt", 'r')
file_contents = file.read()


bricks = [
    [[int(n) for n in pos.split(',')] for pos in line.split('~')]
    for line in file_contents.splitlines()
]
bricks.sort(key=lambda brick: brick[0][2])
n = len(bricks)


def overlaps(a, b):
    return (
        max(a[0][0], b[0][0]) <= min(a[1][0], b[1][0]) and \
        max(a[0][1], b[0][1]) <= min(a[1][1], b[1][1])
    )


for i, brick in enumerate(bricks):
    z = 1
    for j in range(i):
        other = bricks[j]
        if overlaps(brick, other):
            z = max(z, other[1][2] + 1)
    
    brick[1][2] = brick[1][2] - (brick[0][2] - z)
    brick[0][2] = z

bricks.sort(key=lambda brick: brick[0][2])


forward_sup = [set() for _ in range(n)]
reverse_sup = [set() for _ in range(n)]

for i, top in enumerate(bricks):
    for j in range(i):
        down = bricks[j]
        if overlaps(down, top) and top[0][2] == down[1][2] + 1:
            forward_sup[j].add(i)
            reverse_sup[i].add(j)


answer = 0

for i in range(n):
    q = [j for j in forward_sup[i] if len(reverse_sup[j]) == 1]
    falling = set(q)
    falling.add(i)

    while q:
        j = q.pop(0)
        for k in forward_sup[j]:
            if k not in falling and falling == reverse_sup[k] | falling:
                q.append(k)
                falling.add(k)

    answer += len(falling) - 1

print(answer)


file = open("day-06/inputs/part_1.txt", 'r')
file_contents = file.read()

lines = file_contents.splitlines()


times = list(map(int, lines[0].split()[1:]))
distances = list(map(int, lines[1].split()[1:]))


product = 1

for i in range(len(times)):
    ways = 0
    for t in range(times[i]):
        speed = t
        dist = (times[i] - t) * speed
        if dist > distances[i]:
            ways += 1
    product *= ways


print(product)

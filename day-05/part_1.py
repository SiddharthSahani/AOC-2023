
file = open("day-05/inputs/part_1.txt", 'r')
file_contents = file.read()
parts = file_contents.split('\n\n')


seeds = list(map(int, parts[0].split(': ')[1].split()))
parts = parts[1:]
num_conversions = len(parts)


conversion_ranges = [[] for _ in range(num_conversions)]

for i in range(num_conversions):
    for line in parts[i].splitlines()[1:]:
        dest_start, src_start, length = map(int, line.split())
        conversion_ranges[i].append((src_start, src_start+length, dest_start))


def get_from_ranges(item, ranges_obj):
    for range_obj in ranges_obj:
        src_start, src_end, dest_start = range_obj
        if item in range(src_start, src_end):
            delta = item - src_start
            return dest_start + delta

    return item


locations = []

for seed in seeds:
    val = seed
    for i in range(num_conversions):
        val = get_from_ranges(val, conversion_ranges[i])
    locations.append(val)


print(min(locations))

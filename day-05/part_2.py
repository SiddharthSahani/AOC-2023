
file = open("day-05/inputs/part_2.txt", 'r')
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


seed_ranges = []
for i in range(len(seeds)//2):
    seed_ranges.append((seeds[i*2], seeds[i*2] + seeds[i*2+1]))


for conversion_range in conversion_ranges:
    new_ranges = []

    while len(seed_ranges) > 0:
        start, end = seed_ranges.pop()

        for src_start, src_end, dest_start in conversion_range:
            overlap_s = max(start, src_start)
            overlap_e = min(end, src_end)

            if overlap_e > overlap_s: # invalid range
                shift = src_start - dest_start
                new_ranges.append((overlap_s - shift, overlap_e - shift))

                # the leftover ranges
                if overlap_s > start:
                    seed_ranges.append((start, overlap_s))
                if overlap_e < end:
                    seed_ranges.append((overlap_e, end))

                break

        else:
            new_ranges.append((start, end))
    
    seed_ranges = new_ranges


print(min(seed_ranges)[0])

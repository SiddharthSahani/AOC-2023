
from functools import cache


file = open("day-12/inputs/part_1.txt")
file_contents = file.read()


@cache
def solve(line, records, pos, cur_hash_count, num_hash_counts):
    if len(line) == pos:
        if len(records) == num_hash_counts and cur_hash_count == 0: # all grps done
            return 1
        if len(records) == num_hash_counts + 1 and cur_hash_count == records[-1]: # last correct grp
            return 1
        return 0

    chars = line[pos]
    if chars == '?':
        chars = '.#'

    res = 0

    for c in chars:
        if c == '.':
            if cur_hash_count == 0:
                res += solve(line, records, pos+1, 0, num_hash_counts)
            elif num_hash_counts < len(records) and records[num_hash_counts] == cur_hash_count:
                res += solve(line, records, pos+1, 0, num_hash_counts+1)
        else:
            res += solve(line, records, pos+1, cur_hash_count+1, num_hash_counts)

    return res


total = 0

for i, line in enumerate(file_contents.splitlines()):
    line, records = line.split()
    records = tuple(int(rec) for rec in records.split(','))
    total += solve(line, records, 0, 0, 0)

print(total)

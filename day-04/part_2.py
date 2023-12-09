
file = open("day-04/inputs/part_2.txt", 'r')
file_contents = file.read()


lines = file_contents.splitlines()
N = len(lines)
copies = [0 for _ in range(N)]

for id, line in enumerate(lines):
    numbers, winning_numbers = line.split(': ')[1].split(' | ')

    matches_set = set(numbers.split()) & set(winning_numbers.split())
    num_matches = len(matches_set)

    instances = copies[id] + 1
    for i in range(num_matches):
        copies[id + i + 1] += instances

print(sum(copies) + N)

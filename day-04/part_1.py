
file = open("day-04/inputs/part_1.txt", 'r')
file_contents = file.read()


total_score = 0

for id, line in enumerate(file_contents.splitlines()):
    numbers, winning_numbers = line.split(': ')[1].split(' | ')

    matches_set = set(numbers.split()) & set(winning_numbers.split())
    num_matches = len(matches_set)
    card_score = 0 if num_matches == 0 else 2 ** (num_matches - 1)
    total_score += card_score

print(total_score)


from functools import reduce


file = open("day-02/inputs/part_2.txt", 'r')
file_contents = file.read()


sum_pows = 0


for id, line in enumerate(file_contents.splitlines(), start=1):
    three_sets = line.split(': ')[1].split('; ')

    max_items = [0, 0, 0]

    for set in three_sets:
        for item in set.split(', '):
            item = item.split()
            match item[1]:
                case 'red':
                    max_items[0] = max(max_items[0], int(item[0]))
                case 'green':
                    max_items[1] = max(max_items[1], int(item[0]))
                case 'blue':
                    max_items[2] = max(max_items[2], int(item[0]))

    sum_pows += reduce(lambda a, b: a*b, max_items, 1)


print(sum_pows)

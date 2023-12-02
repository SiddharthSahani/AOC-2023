
file = open("day-02/inputs/part_1.txt", 'r')
file_contents = file.read()

actual = [12, 13, 14] # R G B

sum_ids = 0


for id, line in enumerate(file_contents.splitlines(), start=1):
    three_sets = line.split(': ')[1].split('; ')

    valid = True

    for set in three_sets:
        set_items = [0, 0, 0]
        for item in set.split(', '):
            item = item.split()
            match item[1]:
                case 'red':
                    set_items[0] = int(item[0])
                case 'green':
                    set_items[1] = int(item[0])
                case 'blue':
                    set_items[2] = int(item[0])

        if any(set_items[i] > actual[i] for i in range(3)):
            valid = False
            break
        
    if valid:
        sum_ids += id


print(sum_ids)


file = open("day-09/inputs/part_2.txt", 'r')
file_contents = file.read()


sum_vals = 0

for line in file_contents.splitlines():
    values = [[int(x) for x in line.split()][::-1]]

    while not all(val == 0 for val in values[-1]):
        diff_seq = [values[-1][i+1] - values[-1][i] for i in range(len(values[-1])-1)]
        values.append(diff_seq)

    values[-1].append(0)
    for i in range(2, len(values)+1):
        seq = values[-i]
        seq.append(seq[-1] + values[-i+1][-1])

    sum_vals += values[0][-1]


print(sum_vals)

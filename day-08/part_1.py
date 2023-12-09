
file = open("day-08/inputs/part_1.txt", 'r')
file_contents = file.read()


seq, nodes = file_contents.split('\n\n')
lr_nodes = {}


for id, line in enumerate(nodes.splitlines()):
    node, lr = line.split(' = ')
    l, r = lr[1:-1].split(', ')
    lr_nodes[node] =  [l, r]


num_steps = 0

cur_node = 'AAA'
while cur_node != 'ZZZ':
    inst = seq[num_steps % len(seq)]
    cur_node = lr_nodes[cur_node][0 if inst == 'L' else 1]
    num_steps += 1

print(num_steps)

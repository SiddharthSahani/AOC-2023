
from math import lcm


file = open("day-08/inputs/part_2.txt", 'r')
file_contents = file.read()


seq, nodes = file_contents.split('\n\n')
lr_nodes = {}


for id, line in enumerate(nodes.splitlines()):
    node, lr = line.split(' = ')
    l, r = lr[1:-1].split(', ')
    lr_nodes[node] =  [l, r]


num_steps = []
cur_nodes = [node for node in lr_nodes if node[2] == 'A']

for cur_node in cur_nodes:
    num_step = 0
    while cur_node[2] != 'Z':
        inst = seq[num_step % len(seq)]
        cur_node = lr_nodes[cur_node][0 if inst == 'L' else 1]
        num_step += 1
    num_steps.append(num_step)

print(lcm(*num_steps))

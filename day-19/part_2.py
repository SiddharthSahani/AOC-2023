
file = open("day-19/inputs/part_2.txt", 'r')
file_contents = file.read()


xmas = {k: v for k, v in zip("xmas", range(4))}

def parse_rule(rule):
    if ':' in rule:
        condition, result = rule.split(':')
        char, op = condition[:2]
        n = int(condition[2:])
        return (xmas[char], op, n, result)
    return rule


def parse_workflow(workflow):
    b_idx = workflow.index('{')
    name = workflow[: b_idx]
    rules = workflow[b_idx+1: -1].split(',')
    return name, [parse_rule(rule) for rule in rules]


def parse_part(part):
    compos = part[1:-1].split(',')
    return tuple(int(compo[2:]) for compo in compos)


workflows, parts = file_contents.split('\n\n')

workflow_map = {}
for workflow in workflows.splitlines():
    name, rules = parse_workflow(workflow)
    workflow_map[name] = rules

parts = [parse_part(part) for part in parts.splitlines()]


def count(ranges, wf_name):
    if wf_name == 'R':
        return 0

    if wf_name == 'A':
        p = 1
        for r in ranges:
            p *= r[1] - r[0] + 1
        return p

    t = 0

    for rule in workflow_map[wf_name]:
        if isinstance(rule, tuple):
            char, op, n, result = rule
            r = ranges[char]            
            range_t = (r[0], min(n-1, r[1])) if op == '<' else (max(n+1, r[0]), r[1])
            range_f = (max(n, r[0]),   r[1]) if op == '<' else (r[0],   min(n, r[1]))

            if range_t[0] <= range_t[1]:
                copy = ranges[:]
                copy[char] = range_t
                t += count(copy, result)
            if range_f[0] <= range_f[1]:
                ranges = ranges[:]
                ranges[char] = range_f
            else:
                break
        else:
            t += count(ranges, rule)

    return t


ranges = [(1, 4000)] * 4
print(count(ranges, "in"))


file = open("day-19/inputs/part_1.txt", 'r')
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


def check(part, wf_name):
    if wf_name == 'R':
        return False
    if wf_name == 'A':
        return True

    for rule in workflow_map[wf_name]:
        if isinstance(rule, tuple):
            char, op, n, result = rule
            if op == '<' and part[char] < n:
                return check(part, result)
            if op == '>' and part[char] > n:
                return check(part, result)
        else:
            return check(part, rule)


answer = sum(sum(part) for part in parts if check(part, 'in'))
print(answer)


file = open("day-20/inputs/part_1.txt", 'r')
file_contents = file.read()


modules = {}

for line in file_contents.splitlines():
    module, outputs = line.split(' -> ')
    outputs = outputs.split(', ')

    if module == 'broadcaster':
        module = f"B{module}"

    m_type = module[0]
    m_name = module[1:]

    if m_type == '%': # flip-flops
        modules[m_name] = [m_type, m_name, outputs, "off"]
    elif m_type == '&': # conjunction
        modules[m_name] = [m_type, m_name, outputs, {}]
    else: # broadcaster
        modules[m_name] = [m_type, m_name, outputs, None]

for name, mod in modules.items():
    for out in mod[2]:
        if out in modules and modules[out][0] == '&':
            modules[out][3][name] = 'lo'


n_lo = 0
n_hi = 0

for _ in range(1000):
    queue = [
        ("broadcaster", out, "lo")
        for out in modules["broadcaster"][2]
    ]
    n_lo += 1

    while queue:
        name, out, pulse = queue.pop(0)

        if pulse == 'lo':
            n_lo += 1
        else:
            n_hi += 1
        
        if out not in modules:
            continue

        module = modules[out]

        if module[0] == '%' and pulse == 'lo':
            module[3] = 'on' if module[3] == 'off' else 'off'
            out_pulse = 'hi' if module[3] == 'on' else 'lo'
            for out in module[2]:
                queue.append((module[1], out, out_pulse))

        elif module[0] == '&':
            module[3][name] = pulse
            out_pulse = 'lo' if all(val == 'hi' for val in module[3].values()) else 'hi'
            for out in module[2]:
                queue.append((module[1], out, out_pulse))

print(n_lo * n_hi)

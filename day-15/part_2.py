
file = open("day-15/inputs/part_2.txt")
file_contents = file.read()


items = file_contents.split(',')


def h(item):
    val = 0
    for c in item:
        val += ord(c)
        val *= 17
        val %= 256
    return val


boxes = [[] for _ in range(256)]

for item in items:
    if '=' in item:
        label, n = item.split('=')
        hash = h(label)
        for i, thing in enumerate(boxes[hash]):
            if thing[0] == label:
                boxes[hash][i] = (label, int(n))
                break
        else:
            boxes[hash].append((label, int(n)))
    else:
        label = item[:-1]
        hash = h(label)
        for i, thing in enumerate(boxes[hash]):
            if thing[0] == label:
                boxes[hash].pop(i)
                break


answer = 0

for i, box in enumerate(boxes, start=1):
    for j, thing in enumerate(box, start=1):
        answer += i * j * thing[1]

print(answer)

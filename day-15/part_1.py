
file = open("day-15/inputs/part_1.txt")
file_contents = file.read()


items = file_contents.split(',')


answer = 0

for item in items:
    val = 0
    for char in item:
        val += ord(char)
        val *= 17
        val %= 256
    answer += val

print(answer)

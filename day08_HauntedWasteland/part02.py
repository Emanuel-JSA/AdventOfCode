import math

# input_data = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

with open('data.txt', 'r') as file:
    input_data = file.read()

lines = input_data.split("\n")
instructions = lines.pop(0)
lines.pop(0)
dict_lines = {}

for line in lines:
    key, value = line.split('=')
    value = value.replace('(', '').replace(')', '')  # remove '(' and ')'
    value = tuple(val.strip() for val in value.split(','))
    dict_lines[key.strip()] = value

pos = [key for key in dict_lines if key.endswith('A')]
steps_count = []

for p in pos:
    steps = 0
    while not p.endswith('Z'):
        for i in instructions:
            steps += 1
            if i == 'L':
                p = dict_lines[p][0]
            elif i == 'R':
                p = dict_lines[p][1]
            if p.endswith('Z'):
                break
    steps_count.append(steps)

print(math.lcm(*steps_count))
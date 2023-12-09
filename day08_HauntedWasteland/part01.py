# input_data = """LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""

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

pos = 'AAA'
steps = 0
while pos != 'ZZZ':
    for i in instructions:
        steps += 1
        if i == 'L':
            pos = dict_lines[pos][0]
        elif i == 'R':
            pos = dict_lines[pos][1]

print(steps)
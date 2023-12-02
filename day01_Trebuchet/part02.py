# input_data = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen"""

with open('data.txt', 'r') as file:
    input_data = file.read()

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

input_lines = input_data.splitlines()

def find_digit(line: str, last=False):

    start = 0
    stop = len(line) + 1
    step = 1

    if last:
        start = -1
        stop *= -1
        step *= -1
    
    for i in range(start, stop, step):
        if line[i].isdigit():
            return line[i]
            
        if last:
            substr = line[i:]
        else:
            substr = line[:i + step]

        for word, digit in numbers.items():
            if word in substr:
                return digit

for i in range(len(input_lines)):
    first_digit = find_digit(input_lines[i])
    last_digit = find_digit(input_lines[i], last=True)
    input_lines[i] = first_digit + last_digit

sum_val = sum(map(int, input_lines))
print(sum_val)

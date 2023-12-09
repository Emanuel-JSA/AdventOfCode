# input_data = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""

with open('data.txt', 'r') as file:
    input_data = file.read()

lines = input_data.split("\n")

values = []

def get_final_value(numbers):
    diffs = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
    if all(v == 0 for v in diffs):
        return numbers[-1] + diffs[-1]
    else:
        return numbers[-1] + get_final_value(diffs)
        
for line in lines:
    numbers = [int(n) for n in line.split()]
    value = get_final_value(numbers)
    values.append(value)
            
print(sum(values))
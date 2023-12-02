import re

with open('data.txt', 'r') as file:
    input = file.read()

# separate each line into a list
input = input.splitlines()

# clean the list removing all non-numeric characters
for i in range(len(input)):
    digits = re.sub("[^0-9]", "", input[i])

    # get first and last digit
    if len(digits) == 1:
        first = digits[0]
        last = digits[0]
    else:
        first = digits[0]
        last = digits[-1]
        
    input[i] = first + last

# sum all digits
sumVal = sum(map(int, input))
print(sumVal)

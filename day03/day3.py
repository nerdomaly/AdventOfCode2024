import re

matchString = r"mul\(([0-9]+)\,([0-9]+)\)"
disabledMatch = r"don't\(\).+?do\(\)" 

# open input.txt file and return regex matches
with open('input.txt') as fh:
    input = fh.read()

    matches = re.findall(matchString, input)
    # sum of the product of the two numbers in each match
    print("Sum of the product of matches:", sum([int(x) * int(y) for x, y in matches]))

    # remove all instances of the disabledMatch
    input = re.sub(disabledMatch, "", input, flags=re.DOTALL)
    matches = re.findall(matchString, input)
    print("Sum of the product of matches with disabled removed:", sum([int(x) * int(y) for x, y in matches]))

# Python made me angry with this one. I had the solution, but didn't know I had to
# use the re.DOTALL flag to get it to include newlines in the + match. So I was slightly
# off on the second part of the problem until I realized that.
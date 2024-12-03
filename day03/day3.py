import re

matchString = r"mul\(([0-9]+)\,([0-9]+)\)"

# open input.txt file and return regex matches
with open('input.txt') as fh:
    matches = re.findall(matchString, fh.read())

    # sum of the product of the two numbers in each match
    print("Sum of the product of matches:", sum([int(x) * int(y) for x, y in matches]))

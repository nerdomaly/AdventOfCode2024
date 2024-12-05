import re

orderPattern = re.compile(r'([0-9]+)\|([0-9]+)')
orderInstructions = []
printInstructions = []

goodInstructionMiddlePageSum = 0

with open("input.txt") as fh:
    for line in fh:
        line = line.strip()

        if not line:
            continue

        inputMatch = re.match(orderPattern, line)

        if inputMatch:
            orderInstructions.append(line)
        else:
            printInstructions.append(line)

for instructionLine in printInstructions:
    instructions = instructionLine.split(',')

    goodInstruction = True

    for order in orderInstructions:
        (pre, post) = re.match(orderPattern, order).groups()

        if (pre in instructions) and (post in instructions):
            if (instructions.index(pre) > instructions.index(post)):
                goodInstruction = False
                break

    middleNum = (len(instructions) - 1)  // 2
    if goodInstruction:
        goodInstructionMiddlePageSum += int(instructions[middleNum])

print("Middle page sum:", goodInstructionMiddlePageSum)
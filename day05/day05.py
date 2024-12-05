import re

orderPattern = re.compile(r'([0-9]+)\|([0-9]+)')
orderInstructions = []
printInstructions = []

goodInstructionMiddlePageSum = 0
badInstructionMiddlePageSum = 0

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

    # problem set one
    for order in orderInstructions:
        (pre, post) = re.match(orderPattern, order).groups()

        if (pre in instructions) and (post in instructions):
            if (instructions.index(pre) > instructions.index(post)):
                goodInstruction = False
                break

    if not goodInstruction:
        # problem set two
        done = False
        while not done:
            done = True

            for order in orderInstructions:
                (pre, post) = re.match(orderPattern, order).groups()

                if (pre in instructions) and (post in instructions):
                    leftIndex, rightIndex = instructions.index(pre), instructions.index(post)

                    if (leftIndex > rightIndex):
                        instructions[leftIndex], instructions[rightIndex] = instructions[rightIndex], instructions[leftIndex]
                        done = False

    middleNum = (len(instructions) - 1)  // 2
    
    goodInstructionMiddlePageSum += int(instructions[middleNum] if goodInstruction else 0)
    badInstructionMiddlePageSum += int(instructions[middleNum] if not goodInstruction else 0)

print("Good Middle page sum:", goodInstructionMiddlePageSum)
print("Bad Middle page sum:", badInstructionMiddlePageSum)
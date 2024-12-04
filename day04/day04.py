solution = "XMAS"
totalCount = 0

def checkSolution(string):
    return string == solution or string[::-1] == solution


puzzle = open('input.txt').readlines()

for y in range(len(puzzle)):
    puzzleLine = puzzle[y].strip()
    print(f'puzzle line [{y}]:', puzzleLine)

    for x in range(len(puzzleLine)):
        if (x + 3 < len(puzzleLine)):
            across = puzzleLine[x:x+4]
            totalCount += 1 if checkSolution(across) else 0

        if (y + 3 < len(puzzle)):
            down = ''.join(l for l in [puzzle[y][x], puzzle[y+1][x], puzzle[y+2][x], puzzle[y+3][x]])
            totalCount += 1 if checkSolution(down) else 0

        if (y + 3 < len(puzzle) and x + 3 < len(puzzleLine)):
            backslash = ''.join(l for l in [puzzle[y][x], puzzle[y+1][x+1], puzzle[y+2][x+2], puzzle[y+3][x+3]])
            totalCount += 1 if checkSolution(backslash) else 0

        if (y + 3 < len(puzzle) and x - 3 >= 0):
            forwardslash = ''.join(l for l in [puzzle[y][x], puzzle[y+1][x-1], puzzle[y+2][x-2], puzzle[y+3][x-3]])
            totalCount += 1 if checkSolution(forwardslash) else 0
        
print("Total Count:", totalCount)
solution1 = "XMAS"
solution2 = "MAS"
totalSolution1 = 0
totalSolution2 = 0

def checkSolution(string, solution):
    return string == solution or string[::-1] == solution

puzzle = open('input.txt').readlines()

for y in range(len(puzzle)):
    puzzleLine = puzzle[y].strip()
    # print(f'puzzle line [{y}]:', puzzleLine)

    for x in range(len(puzzleLine)):
        # Check solution 1:
        # Looking for XMAS across, down, backslash, and forwardslash
        if (x + 3 < len(puzzleLine)):
            across = puzzleLine[x:x+4]
            totalSolution1 += 1 if checkSolution(across, solution1) else 0

        if (y + 3 < len(puzzle)):
            down = ''.join(l for l in [puzzle[y][x], puzzle[y+1][x], puzzle[y+2][x], puzzle[y+3][x]])
            totalSolution1 += 1 if checkSolution(down, solution1) else 0

        if (y + 3 < len(puzzle) and x + 3 < len(puzzleLine)):
            backslash = ''.join(l for l in [puzzle[y][x], puzzle[y+1][x+1], puzzle[y+2][x+2], puzzle[y+3][x+3]])
            totalSolution1 += 1 if checkSolution(backslash, solution1) else 0

        if (y + 3 < len(puzzle) and x - 3 >= 0):
            forwardslash = ''.join(l for l in [puzzle[y][x], puzzle[y+1][x-1], puzzle[y+2][x-2], puzzle[y+3][x-3]])
            totalSolution1 += 1 if checkSolution(forwardslash, solution1) else 0
        
        # Check solution 2:
        # Looking for MAS in X pattern
        if (y + 2 < len(puzzle) and x + 2 < len(puzzleLine)):
            backslash = ''.join(l for l in [puzzle[y][x], puzzle[y+1][x+1], puzzle[y+2][x+2]])
            forwardslash = ''.join(l for l in [puzzle[y+2][x], puzzle[y+1][x+1], puzzle[y][x+2]])

            totalSolution2 += 1 if checkSolution(backslash, solution2) and checkSolution(forwardslash, solution2) else 0
            
print("Total Soution 1:", totalSolution1)
print("Total Soution 2:", totalSolution2)
# Everything is Y, X indexed
directions = ['^', '>', 'v', '<']
dirModifier = {'^': [-1, 0], '>': [0, 1], 'v': [1,0], '<': [0, -1] }
curDirIndex = 0
empty, blocker, completed = '.', '#', 'X'
gridSize = 130

with open('input.txt') as f:
    data = f.read().split('\n')

map = [list(item) for item in data]
curLocation = [[i, item.index('^')] for i, item in enumerate(map) if '^' in item != -1][0]

step = 0
while True:
    [y, x] = [curLocation[0] + dirModifier[directions[curDirIndex]][0], curLocation[1] + dirModifier[directions[curDirIndex]][1]]

    if x < 0 or x >= gridSize or y < 0 or y >= gridSize:
        map[curLocation[0]][curLocation[1]] = completed
        break

    if map[y][x] == blocker:
        oldDirIndex = curDirIndex
        curDirIndex = (curDirIndex + 1) % 4
        print(f"traveled {step} then changed direction from {directions[oldDirIndex]} to {directions[curDirIndex]}")
        step = 0
    else:
        map[curLocation[0]][curLocation[1]] = completed
        curLocation = [y, x]

    step += 1

with open('output.txt', 'w') as f:
    for line in map:
        f.write(''.join(line) + '\n')

totalDistictSpaces = [sum(line.count(completed) for line in map)]

print("Total Distinct Spaces:", totalDistictSpaces[0])
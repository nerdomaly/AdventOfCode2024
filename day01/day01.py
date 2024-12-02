leftCol, rightCol, sumDiff  = [], [], 0
simScoreLookup, simScoreTotal = {}, 0

with open('input.txt') as fh:
    for line in fh:
        [left, right] = line.split()
        leftCol.append(int(left))
        rightCol.append(int(right))

# sorting the columns
leftCol.sort()
rightCol.sort()

for i in range(len(leftCol)):
    ## Sum of Differences calculation
    sumDiff += abs(leftCol[i] - rightCol[i])

    ## Similarity Score calculation
    if leftCol[i] in simScoreLookup:
        simScoreTotal += simScoreLookup[leftCol[i]]
    else:
        count = rightCol.count(leftCol[i])
        simScoreLookup[leftCol[i]] = count * leftCol[i]
        simScoreTotal += simScoreLookup[leftCol[i]]

print("Sum of Differences:", sumDiff)
print("Similarity Score:", simScoreTotal)
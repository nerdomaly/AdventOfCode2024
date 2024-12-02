totalSafeNoDampener = 0
totalSafeWithDampener = 0

def isSorted(row):
    sortedAsc = sorted(row, key=int)
    sortedDesc = sorted(row, key=int, reverse=True)

    return row == sortedAsc or row == sortedDesc

def safePairs(pairs):
    safeArray = list(map(lambda x: True if abs(x[0] - x[1]) >= 1 and abs(x[0] - x[1]) <= 3 else False, pairs))

    return all(x == True for x in safeArray)

with open('input.txt') as fh:
    for line in fh:
        row = list(map(int, line.split()))

        if (isSorted(row) and safePairs(zip(row, row[1:]))):
            totalSafeNoDampener += 1
        else:
            for index in range(len(row)):
                dampened = [x for i, x in enumerate(row) if i != index]

                if (isSorted(dampened)) and safePairs(zip(dampened, dampened[1:])):
                    totalSafeWithDampener += 1
                    break

print("Total Safe No Dampener:", totalSafeNoDampener)
print("Total Safe Dampener:", totalSafeWithDampener)
print("Total Safe:", totalSafeNoDampener + totalSafeWithDampener)
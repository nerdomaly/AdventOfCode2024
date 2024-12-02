totalSafe = 0

def safePairs(pairs):
    safeArray = list(map(lambda x: True if abs(x[0] - x[1]) >= 1 and abs(x[0] - x[1]) <= 3 else False, pairs))

    return all(x == True for x in safeArray)

with open('input.txt') as fh:
    for line in fh:
        row = list(map(int, line.split()))

        sortedAsc = sorted(row, key=int)
        sortedDesc = sorted(row, key=int, reverse=True)

        if (row == sortedAsc or row == sortedDesc):
            safe = safePairs(zip(row, row[1:]))

            totalSafe += 1 if safe else 0

print("Total Safe:", totalSafe)
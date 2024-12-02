leftcol = []
rightcol = []
sumdiff = 0

with open('input.txt') as fh:
    for line in fh:
        [left, right] = line.split()
        leftcol.append(int(left))
        rightcol.append(int(right))

# sorting the columns
leftcol.sort()
rightcol.sort()

for i in range(len(leftcol)):
    sumdiff += abs(leftcol[i] - rightcol[i])

print(sumdiff)
from sys import stdin
import math

lines = stdin.read().splitlines()
lines_copy = [list(line) for line in lines] 


length, breadth, racketSize = lines[0].split(" ")
length, breadth, racketSize = int(length), int(breadth), int(racketSize)

maxBees = -math.inf

row = -1
col = -1

for i in range(1, length - racketSize + 2):
    for j in range(0, breadth - racketSize + 2):
        subBees = 0

        for a in range(i+1, racketSize + i - 1):
            for b in range(j+1, racketSize + j - 1):
                subBees += int(lines[a][b] == "*")
        
        if subBees > maxBees:
            maxBees = subBees

            row, col = i, j 

if (row != -1 and col != -1):
    for i in range(row, racketSize + row):
        for j in range(col, racketSize + col):
            if i == row or i == row + racketSize - 1:
                if j == col or j == col + racketSize - 1:
                    lines_copy[i][j] = "+"
                else:
                    lines_copy[i][j] = "-"

            elif j == col or j == col + racketSize - 1:
                lines_copy[i][j] = "|"

            else:
                continue

maxBees = 0 if maxBees < 0 else maxBees

print(maxBees)

for line in lines_copy[1:]:
        print("".join(line))    
        
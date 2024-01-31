from sys import stdin
import sys

lines = stdin.read().splitlines()

#counter for first itr
fcnt = int(lines[0])

# constant cost
ccost = 0.08

start = 1

while lines:
    
    prevTime = 0

    for i in range (start, fcnt + start):
        
        time, rev = lines[i].split(" ")
        time, rev = int(time), float(rev)

        lines[i] = time, rev - (ccost * (time - prevTime))

        prevTime = time

    maxSoFar = -sys.maxsize - 1
    maxEndingHere = 0
    startTime = 0
    endTime = 0
    
    for i in range (start, fcnt + start):
        prof = lines[i][1]

        maxEndingHere += prof

        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere

            if startTime != 0:
                startTime = lines[i][0]

            endTime = lines[i][0]

        if maxEndingHere < 0:
            maxEndingHere = 0

    print(maxSoFar, startTime, endTime)
        
    start += fcnt

    fcnt = int(lines[start])

    start += 1

    if fcnt == 0:
        break

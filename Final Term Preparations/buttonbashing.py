from sys import stdin, setrecursionlimit
import math
from collections import deque

setrecursionlimit(10 ** 6)

def bfs(buttons, distArray, queue):
 
    while queue:
        v = queue.popleft()
        d = distArray[v]
        
        
        for button in buttons:
            vertex = button + v 
            if vertex >= len(distArray):
                vertex = 3600
            if vertex < 0:
                vertex = 0     
            if distArray[vertex] > d + 1:
                distArray[vertex] = d + 1
                queue.append(vertex)


     



lines = stdin.read().splitlines()

nOfTests = int(lines[0])

for i in range(1, nOfTests * 2, 2):
    nOfButtons, target = lines[i].split(" ")
    nOfButtons, target = int(nOfButtons), int(target)

    buttons = lines[i + 1].split(" ")
    lb = len(buttons)

    for i in range(lb):
        buttons[i] = int(buttons[i])
        
    
    distArray = [math.inf] * 3601 

    queue = deque()

    queue.append(0)
    distArray[0] = 0

    bfs(buttons, distArray, queue)

    count = 0
    index = target

    while True:
        
        if distArray[index] != math.inf:
            
            break
        else:
            count += 1
            index += 1

    print(str(distArray[index]) + " " + str(count))

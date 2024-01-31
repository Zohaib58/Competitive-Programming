from sys import stdin
import heapq
import math

lines = stdin.read().splitlines()

def isValid(row, col):
    if (row < 0 or row >= lrow):
        return False
    if (col < 0 or col >= lcol):
        return False
    """    if (isVisited[i][j]):
        return False
    """    
    return True

def dijkstra(graph, source):
    

    minheap = []

    dist = [[float('inf') for _ in range(lcol)] for _ in range(lrow)]
    parent = [[-1 for _ in range(lcol)] for _ in range(lrow)]

    heapq.heappush(minheap, [0, -1, -1])

    while minheap:
        distU, vRow, vCol = heapq.heappop(minheap)

        if vRow == -1 and vCol == -1:
            for i in range(lcol):
                if (distU + graph[0][i]) < dist[0][i]:
                    parent[0][i] = (0, 0)
                    dist[0][i] = distU + graph[0][i]
                    heapq.heappush(minheap, [dist[0][i], 0, i]) 
        else:
            toVisit = [(vRow - 1, vCol), (vRow + 1, vCol), (vRow, vCol - 1), (vRow, vCol + 1), (vRow - 1, vCol - 1), (vRow + 1, vCol - 1),
                       (vRow + 1, vCol + 1), (vRow - 1, vCol + 1)]
            
            for arr in toVisit:
                if isValid(arr[0], arr[1]):
                    if (distU + graph[arr[0]][arr[1]]) < dist[arr[0]][arr[1]]:
                        parent[arr[0]][arr[1]] = (vRow, vCol)
                        dist[arr[0]][arr[1]] = distU + graph[arr[0]][arr[1]]
                        heapq.heappush(minheap, [ dist[arr[0]][arr[1]], arr[0], arr[1]])
                

    return dist, parent

start = 0
while(True):

    rows, cols = lines[start].split(" ")
    rows, cols = int(rows), int(cols)

    if (rows == 0 and cols == 0):
        break

    
    array = []
    start += 1

    for i in range(start, rows + start):
        array.append(list(lines[i]))

        for arr in array:
            l = len(arr)
            for i in range(l):
                arr[i] = int(arr[i])
        
        global lrow
        global lcol

        lrow = len(array)
        lcol = len(array[0])

    distArray, parentArray = dijkstra(array, -1)

    
    """To find min from last row"""
    min = math.inf
    counter = 0
    index = 0


    for element in distArray[-1]:
        
        if element < min:
            min = element
            index = counter
        counter += 1

    """                          """

    minVertex = (len(distArray) - 1, index)

    parent = minVertex

    while parent != (0,0):
        array[parent[0]][parent[1]] = " "
        parent = parentArray[parent[0]][parent[1]] 

    for arr in array:
        for el in arr:
            print(el, end = "")
        print()
    print()

    start += rows
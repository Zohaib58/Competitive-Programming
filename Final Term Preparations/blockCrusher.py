import math
import heapq
from sys import stdin

def isValid(x, y):
    if x < 0 or x >= row or y < 0 or y >= col:
        return False

    return True

def neighbor(u, x , y):
    neighbors = []

    if isValid((x-1), y):
        neighbors.append((x-1, y))

    if isValid(x, (y-1)):
        neighbors.append((x, (y-1)))

    if isValid((x+1), y):
        neighbors.append(((x+1), y))

    if isValid(x, (y+1)):
        neighbors.append((x, (y+1)))

    if isValid(x+1, (y+1)):
        neighbors.append((x+1, (y+1)))

    if isValid(x-1, (y-1)):
        neighbors.append((x-1, (y-1)))

    if isValid(x-1, (y+1)):
        neighbors.append((x-1, (y+1)))

    if isValid(x+1, (y-1)):
        neighbors.append((x+1, (y-1)))

    return neighbors

input_matrix = [[2, 2, 8, 1, 4, 3, 1],
                [2, 3, 2, 9, 4, 6, 3],
                [7, 1, 8, 3, 8, 3, 9]]
#row = len(input_matrix)
#col = len(input_matrix[0])

def blockCrusher(graph, s):
    rows, cols = len(graph), len(graph[0])
    # Initialize a 2D array with tuples (-1, -1)
    parent = [[(-1, -1) for _ in range(cols)] for _ in range(rows)]
    #print(parent)

    distances = [[(math.inf) for _ in range(cols)] for _ in range(rows)]
    source_distances = 0
    #print("distances: ", distances)
    j = 0

    minHeap = []
    heapq.heappush(minHeap, (source_distances, s, (-1, -1)))

    while minHeap:
        dist_u, u, index = heapq.heappop(minHeap)
        neighbors = []
        #print("dist_u", dist_u)
        #print("u", u)
        #print("index", index)

        if index == (-1, -1):
            i = 0
            # If index is (-1, -1), it means this is the initial vertex,
            # so we want to consider neighbors in the same row.
            neighbors.extend(graph[u])
            for v in neighbors:
                if distances[0][i] > dist_u + graph[0][i]:
                    distances[0][i] = dist_u + graph[0][i]
                    if (distances[0][i], v) not in minHeap:
                        heapq.heappush(minHeap, (distances[0][i], v, (0,i)))
                        parent[0][i] = index
                i = i + 1

        else: 
            neighbors = neighbor(u, index[0], index[1])
          #  print("neighbours: ", u, j, neighbors)

            for v in neighbors:
                input = graph[v[0]][v[1]]
                if distances[v[0]][v[1]] > dist_u + input:
                    distances[v[0]][v[1]]= dist_u + input
                    if (distances[v[0]][v[1]], input) not in minHeap:
                        heapq.heappush(minHeap, (distances[v[0]][v[1]], input, (v)))
                        parent[v[0]][v[1]] = index

            j = j + 1

    #print(parent)
    #print("distance: ", distances)

    minDis = min(distances[len(distances)-1])

    #print("minDis: ", minDis)
 
    minDisIndex = distances[len(distances)-1].index(minDis)
    index = (len(distances)-1, minDisIndex)
    #print("index: ", index)

    #print("Mindisindex: ", minDisIndex)

    minVertex = (index[0], index[1])

    parentArr = minVertex

    while parentArr != (-1,-1):
        graph[parentArr[0]][parentArr[1]] = " "
        parentArr = parent[parentArr[0]][parentArr[1]] 

    for arr in graph:
        for el in arr:
            print(el, end = "")
        print()
    print()

    


lines = stdin.read().splitlines()
#print(lines)

start = 0
while(True):

    lrows, lcols = lines[start].split(" ")
    #print(lines[start])
    lrows, lcols = int(lrows), int(lcols)

    if (lrows == 0 and lcols == 0):
        break

    
    array = []
    start += 1

    for i in range(start, lrows + start):
        array.append(list(lines[i]))

        for arr in array:
            l = len(arr)
            for i in range(l):
                arr[i] = int(arr[i])
        
        global row
        global col

        row = len(array)
        col = len(array[0])
    blockCrusher(array, 0)
    start += lrows




from sys import stdin
import math
import heapq

lines = stdin.read().splitlines()

global row, col
col, row = lines[0].split(" ")
col, row = int(col), int(row)

global result

start = 1

def dijkstra(graph, source):
    dist = [math.inf] * col
    result = [math.inf] * col

    dist[source] = 0
    minheap = []

    res = 0
    heapq.heappush(minheap, [0, source])
    
    while minheap:
        distU, u = heapq.heappop(minheap)

        if dist[int(u)] < distU:
            continue

        

        for values in graph[u]:
            val = -math.log(values[1])
            if dist[int(values[0])] > distU + val:
                dist[int(values[0])] = distU + val
                result[int(values[0])] = values[1]
                heapq.heappush(minheap, [dist[int(values[0])], values[0]])

    return result






done = False
while row != 0 and col != 0:
    a = {}
    for i in range(start, start + row):
        v1, v2, edge = lines[i].split(" ")
        v1, v2, edge = float(v1), float(v2), float(edge)

        if v1 not in a:
            a[v1] = []
        
        if v2 not in a:
            a[v2] = []

        
        a[v1].append([v2, edge])
        a[v2].append([v1, edge])

    array = dijkstra(a, 0)

    res = 1

    for arr in array[1:]:
        res *= arr
        
    print("{:.4f}".format(res))

    start += col

    done = False
    if start > len(lines) - 1:
        done = True
        break

    col, row = lines[start].split(" ")
    
    col, row = int(col), int(row)
    start += 1


    


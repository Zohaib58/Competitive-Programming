import heapq

times = [[1,2,1]]
n = 2
k = 2

adjList = {}

# Building adjList
for n1, n2, time in times:
    
    if n1 not in adjList:
        adjList[n1] = []

    adjList[n1].append([n2, time])

# Applying Dijkstra
minHeap = [[0, k]]
res = -1
visited = set()

while minHeap:
    d1, n1 = heapq.heappop(minHeap)

    res = d1

    if n1 in adjList:
        for n2, d2 in adjList[n1]:
            if n2 not in visited:
                visited.add(n2)
                heapq.heappush(minHeap, [d2 + d1, n2])

print(res)



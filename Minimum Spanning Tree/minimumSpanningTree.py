from sys import stdin
import math

lines = stdin.read().splitlines()

def createMST(adjList, listOfNodes):
    mstSet = set()

    while listOfNodes:
        mstSet.add(listOfNodes.pop(0)) 
        minimumVal = math.inf

        valToadd = -1
        key = -1
        for data in mstSet:
            for values in adjList[data]:
                if values[1] not in mstSet:
                    if values[1] < minimumVal:
                        minimumVal = values[1]
                        valToadd = values[0]
                        key = data

        mstSet.add((key, valToadd))        

    return mstSet    


nodes, edges = lines[0].split(" ") 
nodes, edges = int(nodes), int(edges)
listOfNodes = [x for x in range(nodes)]

start = 1

while nodes != 0 or edges != 0:
    adjList = {}
    for i in range(start, start + edges):
        node, neighbour, weight = lines[i].split(" ")

        if node not in adjList:
            adjList[node] = []
        
        adjList[node].append([neighbour, weight])


    mst = createMST(adjList, listOfNodes)
    
    # total Cost
    # set traversing


    lineToRead = edges + 2

    nodes, edges = lines[lineToRead].split(" ") 
    start = lineToRead + 1
    nodes, edges = int(nodes), int(edges)

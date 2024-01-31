from sys import stdin
lines = stdin.read().splitlines()

fileChanged = lines[-1]

def makeGraph(lines):
    l = len(lines)
    graph = {}
    for i in range(1, l - 1):
        parts = lines[i].split(':')
        file = parts[0].strip()
        dependencies = parts[1].strip()

        for dependency in dependencies:
            if dependency not in graph:
                dependencies[dependency] = []
            dependencies[dependency].append(file)
        
        
    return graph

graph = makeGraph(lines)



def dfs(s, graph):
    
    stack.append(s)
    neighbors = []
    neighbors.append(graph[s])
    stack.append(neighbors)

    while neighbors:
        neighbor = neighbors.pop()
        for value in graph[neighbor]:
            

    


    
            
    
global stack
stack = []
print(graph)
dfs(fileChanged, graph)
print(stack)
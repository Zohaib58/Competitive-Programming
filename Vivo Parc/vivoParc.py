from sys import stdin

lines = stdin.read().splitlines()
encl =  int(lines[0])

a = {} 
l = len(lines)

# graph
for i in range(1, l):
    key, val = lines[i].split("-")
    key, val = int(key), int(val)
    
    if key not in a:
        a[key] = []

    if val not in a[key]:
        a[key].append(val)
        if val not in a:
            a[val] = []
        a[val].append(key)


def graph_coloring(graph):
    # Initialize an array to store the color assigned to each vertex
    colors = [0] * encl

    # Start the coloring process from the first vertex
    if graph_coloring_util(graph, colors, 1):
        for i in range(1, len(colors) + 1):
            print(str(i) + " " + str(colors[i - 1]))


def graph_coloring_util(graph, colors, vertex):
    # Base case: All vertices are colored
    if vertex == encl + 1:
        return True

    # Try assigning colors to the current vertex
    for color in range(1, 5):
        if is_safe(graph, colors, vertex, color):
            # Assign the color and move on to the next vertex
            colors[vertex - 1] = color

            # Recur to the next vertex
            if graph_coloring_util(graph, colors, vertex + 1):
                return True

            # Backtrack if the current assignment does not lead to a solution
            colors[vertex - 1] = 0

    # If no color can be assigned to the current vertex
    return False


def is_safe(graph, colors, vertex, color):
    # Check if the current color is not used by any adjacent vertices
    for neighbor in graph[vertex]:
        if colors[neighbor - 1] == color:
            return False
    return True

graph_coloring(a)



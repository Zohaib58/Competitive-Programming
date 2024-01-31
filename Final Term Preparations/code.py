# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
from sys import maxint


def maxSubArraySum(a, size):

	max_so_far = -maxint - 1
	max_ending_here = 0

	for i in range(0, size):
		max_ending_here = max_ending_here + a[i]
		if (max_so_far < max_ending_here):
			max_so_far = max_ending_here

		if max_ending_here < 0:
			max_ending_here = 0
	return max_so_far

# Dynamic programming Python implementation
# of LIS problem


# lis returns length of the longest
# increasing subsequence in arr of size n
def lis(arr):
	n = len(arr)

	# Declare the list (array) for LIS and
	# initialize LIS values for all indexes
	lis = [1]*n

	# Compute optimized LIS values in bottom up manner
	for i in range(1, n):
		for j in range(0, i):
			if arr[i] > arr[j] and lis[i] < lis[j] + 1:
				lis[i] = lis[j]+1

	# Initialize maximum to 0 to get
	# the maximum of all LIS
	maximum = 0

	# Pick maximum of all LIS values
	for i in range(n):
		maximum = max(maximum, lis[i])

	return maximum

#0/1
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] 
                              + K[i-1][w-wt[i-1]], 
                              K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 


# Combinational Sum

#Word Break
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


#Graphs
# to make graph
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

#Level Traversal. Check buttonBashing.py for detail
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

# Dijkstra / refer to blockCrusher for parent array and getShorty for reverse
def dijkstra(graph, source):
    dist = [math.inf] * col
    #result = [math.inf] * col

    dist[source] = 0
    minheap = []

    #res = 0
    heapq.heappush(minheap, [0, source])
    
    while minheap:
        distU, u = heapq.heappop(minheap)

        if dist[int(u)] < distU:
            continue

        for values in graph[u]:
            val = -math.log(values[1])
            if dist[int(values[0])] > distU + val:
                dist[int(values[0])] = distU + val
                #result[int(values[0])] = values[1]
                heapq.heappush(minheap, [dist[int(values[0])], values[0]])

    return dist

# M-graph coloring
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


#Bi-partite graph coloring
Algorithm for bipartite graph coloring
The algorithm for bipartite graph coloring is defined as follows:
Traverse all vertices in G using the breadth-first search (BFS).
Choose a vertex and assign the color, say 1.
Assign the color 2 to all of its adjacent vertices.
Apply these steps until all vertices are assigned the colors.


# SCC - strongly connected component/Kosa Raju
from collections import defaultdict

V = 8

adj = defaultdict(list)
rev = defaultdict(list)

def DFS1(i, visited, mystack):
    visited[i] = True
    for j in adj[i]:
        if not visited[j]:
            DFS1(j, visited, mystack)
    mystack.append(i)
def reverse():
    for i in range(V):
        for j in adj[i]:
            rev[j].append(i)
def DFS2(i, visited):
    visited[i] = True
    for j in rev[i]:
        if not visited[j]:
            DFS2(j, visited)
def findSCCs():
    mystack = []
    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            DFS1(i, visited, mystack)

    reverse()

    count_scc = 0
    for i in range(V):
        if not visited[i]:
            DFS2(i, visited)
            count_scc += 1

    print("Number of Strongly Connected Components:", count_scc)
if _name_ == "_main_":

    adj[0].append(1)
    adj[1].append(2)
    adj[2].extend([0, 3])
    adj[3].append(4)
    adj[4].extend([5, 7])
    adj[5].append(6)
    adj[6].extend([4, 7])
    
    findSCCs()


# Topological Sort
In picture


# Permuation
See danceRecital.py

# See geppeto for bitshifting etc

# Kruskal
from sys import stdin

class UFDS:
    def _init_(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.numdisjoint = n

    def find(self, x):
        xp = x
        children = []
        while 0 <= xp < len(self.parents) and xp != self.parents[xp]:
            children.append(xp)
            xp = self.parents[xp]
        for c in children:
            self.parents[c] = xp
        return xp


    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return

        if self.ranks[ap] < self.ranks[bp]:
            self.parents[ap] = bp
            self.sizes[bp] += self.sizes[ap]
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]


"""u = UFDS(8)
print(u.numdisjoint == 8)
u.union(1, 2)
print(u.find(1) == u.find(2))
print(u.find(1) != u.find(3))
print(u.find(2) != u.find(3))
print(u.size(1) == 2)
print(u.size(2) == 2)
print(u.size(3) == 1)
print(u.numdisjoint == 7)
u.union(1, 3)
print(u.find(1) == u.find(2))
print(u.find(1) == u.find(3))
print(u.find(2) == u.find(3))
print(u.find(2) != u.find(4))
print(u.size(1) == 3)
print(u.size(2) == 3)
print(u.size(3) == 3)
print(u.numdisjoint == 6)
u.union(2, 4)
print(u.find(1) == u.find(3))
print(u.find(2) == u.find(4))
print(u.size(1) == 4)
print(u.size(2) == 4)
print(u.numdisjoint == 5)
u.union(2, 3)
print(u.size(1) == 4)
print(u.size(2) == 4)
print(u.numdisjoint == 5)"""

def MST_Kruskal(edges, n):
    edges.sort(key=lambda x: x[2])
    u = UFDS(n)
    mst = []
    for e in edges:
        if u.find(e[0]) != u.find(e[1]):
            u.union(e[0], e[1])
            mst.append(e)
    if len(mst) != n - 1:
        return []
    else:
        return mst



lines = stdin.read().splitlines()


start = 0
while(True):
    edges1 = []
    cost = 0
    result = []

    nodes, edges = lines[start].split(" ")
    #print(lines[start])
    nodes, edges = int(nodes), int(edges)

    if (nodes == 0 and edges == 0):
        break

    
    array = []
    p = []
    q = []
    n = []
    start += 1

    for i in range(start, edges + start):
        array.append(lines[i])

        #for arr in array:
        a, b ,c = map(int, array[-1].split(" "))
        if(a > b):
            a, b = b, a
        p.append(int(a))    
        q.append(int(b))
        n.append(int(c)) 

        
        global row
        global col

        row = len(array)
        col = len(array[0])
    for i in range(len(q)):
        edges1.append((p[i], q[i], n[i]))
    mst_result = MST_Kruskal(edges1, nodes)  # len(set(n)) is the number of vertices
  # max(n) + 1 is the number of vertices
    if (mst_result == []):
        print("Impossible")
    else:
       # print("Minimum Spanning Tree (Kruskal):", mst_result)
        for i in range (len(mst_result)):
            cost += mst_result[i][2]
            result.append((mst_result[i][0], mst_result[i][1]))

        sorted_result = sorted(result)

        
        print(cost)
        for i in range (len(sorted_result)):
            print(sorted_result[i][0], sorted_result[i][1])
       # print(sorted_result)
            

    start += edges
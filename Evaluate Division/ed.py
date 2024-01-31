from collections import defaultdict

def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """

    def buildGraph(equations, values):
        graph = defaultdict(lambda: defaultdict(float))

        le = len(equations)

        for i in range(le):
            a, b = equations[i]

            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]

        return graph    
            
    def dfs(s,d, visited, graph):
        if s not in graph and d not in graph:
            return -1
        if s == d:
            return 1
        
        
        visited.add(s)

        for value in graph[s]:
            if value not in visited:
                res = dfs(value, d, visited, graph) 

                if res != -1:
                    return res * graph[s][value]
        return -1
    
    def calculateQuery(graph, queries):
        resArray = []
        
        for query in queries:
            s, d = query[0], query[1]
            resArray.append(dfs(s, d, set(), graph))

        return resArray
                      


    print(calculateQuery(buildGraph(equations, values), queries))

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

calcEquation(equations, values, queries)
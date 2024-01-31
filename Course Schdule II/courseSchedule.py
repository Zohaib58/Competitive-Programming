def findOrder(numCourses, prerequisites):
    def createGraph(prerequisites):
        graph = {}
        for course, preReq in prerequisites:
        
            if course not in graph:
                graph[course] = []

            graph[course].append(preReq)

        return graph

    def dfs(key, graph, stackSet, toCheck):
        if len(stackSet) == numCourses:
            return 
        
        toCheck.append(key)  
        for value in graph[key]:
            if value in toCheck:
                return -1
            
            
            if value not in stackSet:
                v = 0
                if value in graph:
                    v = dfs(value, graph, stackSet, toCheck)
                if v==-1:
                    return -1
                
                if value not in stackSet:
                    stackSet.append(value)
        
        if key not in stackSet:
            stackSet.append(key)

        return 0
        
        

    graph = createGraph(prerequisites)

    global stackSet 
    stackSet = []
    v = 0
    for key in graph:

        v = dfs(key, graph, stackSet, [])

   
    
    if v != -1:
        l = len(stackSet)
        while l < numCourses:
            stackSet.append(stackSet[-1] + 1 if stackSet else 0)
            l = len(stackSet)
            

    print(stackSet)
    

    
    
numCourses = 3
prerequisites =  [[0,1],[0,2],[1,2]]

findOrder(numCourses, prerequisites)



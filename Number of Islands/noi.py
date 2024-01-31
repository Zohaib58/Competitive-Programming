def isValid(i, j):
    if i < 0 or i >= len(grid):
        return False
    if j < 0 or j >= len(grid[0]):
        return False
    if isVisited[i][j] == True:
        return False
    if grid[i][j] == "0":
        return False

    return True

def dfs(grid, i, j):

    isVisited[i][j] = True
    
    if (isValid(i - 1, j)):
        dfs(grid, i - 1, j)
    
    if (isValid(i + 1, j)):
        dfs(grid, i + 1, j)

    if (isValid(i, j - 1)):
        dfs(grid, i, j - 1)

    if (isValid(i, j + 1)):
        dfs(grid, i, j + 1)


def numIslands(grid):

    noi = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == "1") and (isVisited[i][j] == False):
                dfs(grid, i, j)
                noi += 1
    print(noi)

global grid

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

global isVisited

isVisited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

numIslands(grid)
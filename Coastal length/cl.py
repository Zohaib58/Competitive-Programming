from sys import stdin

lines = stdin.read().splitlines()

rowCount, valueCount = lines[0].split(" ")

rowCount, valueCount = int(rowCount), int(valueCount)

matrix = [[0 for i in range(valueCount + 2)] for j in range(rowCount + 2)]
isVisited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]

for j in range(0, valueCount+2):
    matrix[0][j] = 2
    matrix[rowCount+1][j] = 2

for i in range(1, rowCount+1):
    val = lines[i]
    valArray = [2]
    for k in range(0, valueCount):
        valArray.append(int(val[k]))
    valArray.append(2)

    for j in range(valueCount+2):
        matrix[i][j] = valArray[j]

# print("------------------")
# print(matrix)
# print("------------------")

def isValid(i, j):
    if i < 0 or i >= len(matrix):
        return False
    if j < 0 or j >= len(matrix[0]):
        return False
    if isVisited[i][j] == True:
        return False
    if matrix[i][j] == 1:
        return False

    return True

def dfs(matrix):
    s = [(0, 0)]
    isVisited[0][0] = True

    while len(s) > 0:
        (i,j) = s.pop()
        matrix[i][j] = 2

        if (isValid(i - 1, j)):
            isVisited[i - 1][j] = True
            s.append((i-1, j))

        if (isValid(i + 1, j)):
            isVisited[i + 1][j] = True
            s.append((i+1, j))

        if (isValid(i, j - 1)):
            isVisited[i][j - 1] = True
            s.append((i, j-1))

        if (isValid(i, j + 1)):
            isVisited[i][j + 1] = True
            s.append((i, j+1))




dfs(matrix)

def forRes(matrix):
    res = 0
    for i in range(1, rowCount + 1):
        for j in range(1, valueCount + 1):
            if matrix[i][j] == 1:
                if matrix[i - 1][j] == 2:
                    res += 1
                if matrix[i + 1][j] == 2:
                    res += 1
                if matrix[i][j - 1] == 2:
                    res += 1
                if matrix[i][j + 1] == 2:
                    res += 1
    print(res) 

forRes(matrix)

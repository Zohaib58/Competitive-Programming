def longestIncreasingPath(matrix, lenCol, lenRow):
    def isValid(i, j, lenCol, lenRow):
        if (i < 0 or i >= lenRow):
            return False
        if (j < 0 or j >= lenCol):
            return False
        
        
        
        return True
    
    def dfs(i, j, lenCol, lenRow, matrix, prevResult): 

        if (mat[i][j] != 0):
            return mat[i][j]
        
        mat[i][j] += prevResult + 1

        
        prevVal = matrix[i][j]

        prevResult = mat[i][j]

        down, up, left, right = 0, 0, 0, 0

        if isValid(i-1, j, lenCol, lenRow):
            
            if (matrix[i-1][j] > prevVal):
                
            
                down = dfs(i-1 , j, lenCol, lenRow, matrix, prevResult)

        if isValid(i+1, j, lenCol, lenRow):
            if (matrix[i+1][j] > prevVal):
                
            
                up = dfs(i+1 , j, lenCol, lenRow, matrix, prevResult)
        
        if isValid(i, j - 1, lenCol, lenRow):
            if (matrix[i][j - 1] > prevVal):
                
                
                left = dfs(i , j-1 , lenCol, lenRow, matrix, prevResult)
            
        if isValid(i, j + 1, lenCol, lenRow):
            if (matrix[i][j + 1] > prevVal):
                
                
                right = dfs(i , j+1 , lenCol, lenRow, matrix, prevResult)

        mat[i][j] += max(down, up, left, right)

        return mat[i][j]

    return dfs(lenRow - 1, lenCol - 1, lenCol, lenRow, matrix, 0)

matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]

lenRow = len(matrix)
lenCol = len(matrix[0])

global mat
mat = [[0 for i in range(lenCol)] for j in range(lenRow)]

longestIncreasingPath(matrix, lenCol, lenRow)
print(mat)


def floodFill(sr, sc, lenCol, lenRow, image, color):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type color: int
    :rtype: List[List[int]]
    """
    def isValid(i, j, lenCol, lenRow):
        if (i < 0 or i >= lenRow):
            return False
        if (j < 0 or j >= lenCol):
            return False
        if (isVisited[i][j]):
            return False
        
        return True
    
    def dfs(sr, sc, lenCol, lenRow, image, color): 
        if (image[sr][sc] != toCheckColor):
            return image
        
        image[sr][sc] = color
        isVisited[sr][sc] = True

        if isValid(sr-1, sc, lenCol, lenRow):
            dfs(sr-1 , sc, lenCol, lenRow, image, color)

        if isValid(sr+1, sc, lenCol, lenRow):
            dfs(sr+1 , sc, lenCol, lenRow, image, color)
        
        if isValid(sr, sc - 1, lenCol, lenRow):
            dfs(sr, sc - 1, lenCol, lenRow, image, color)

        if isValid(sr, sc + 1, lenCol, lenRow):
            dfs(sr, sc + 1, lenCol, lenRow, image, color)

        return image

    return dfs(sr, sc, lenCol, lenRow, image, color)
    

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
global toCheckColor
toCheckColor = image[sr][sc]

lenCol = len(image[0])
lenRow = len(image)

global isVisited

isVisited = [[False for i in range(len(image[0]))] for j in range(len(image))]
print(floodFill(sr, sc, lenCol, lenRow, image, color))
    
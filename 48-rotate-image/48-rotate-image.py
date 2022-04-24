class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        #finding a transpose
        
        for i in range(0,n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            matrix[i] = matrix[i][::-1]
        
        
            
        
        
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # finding transpose and reversing every row
        
        n = len(matrix)
        
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            matrix[i] = matrix[i][::-1]
        
        
            
        
        
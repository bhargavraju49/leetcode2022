class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        if m == n:
            for i in range(m):
                for j in range(i+1,n):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j] 
            return matrix
        else:
            res = [[0 for i in range(m)] for i in range(n)]
            
            for i in range(m):
                for j in  range(n):
                    res[j][i] = matrix[i][j]
            
            return res
                
        
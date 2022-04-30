class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        visited = {}
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and visited.get((i,j),0)==0:
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 0
                            visited[(i,k)] = 1
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 0
                            visited[(k,j)] = 1
                    
                        
        
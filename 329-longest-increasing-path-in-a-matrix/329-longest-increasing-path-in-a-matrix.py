class Solution:
    def __init__(self):
        self.max = 0
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cols = len(matrix[0])
        rows = len(matrix)
        dp = [[0 for i in range(cols)] for i in range(rows)]

        def dfs (i,j):
            if dp[i][j]!=0:
                return dp[i][j]
            dir = [[1,0],[-1,0],[0,1],[0,-1]]
            t = 1
            mex = 0
            for a,b in dir:
                newi = a+i
                newj = b+j
                if newi < 0 or newj < 0 or newi >= rows or newj >= cols:
                    continue
                if matrix[newi][newj] > matrix[i][j]:
                    t=t+1
                    k = dfs(newi,newj)
                    dp[newi][newj] = k
                    self.max = max(self.max,k)
                    mex = max(mex,k)
            dp[i][j] = mex+1
            self.max = max(self.max, mex+1)
            return mex+1

        for i in range(rows):
            for j in range(cols):
                if dp[i][j]==0:
                    dfs(i,j)

        return self.max
        pass
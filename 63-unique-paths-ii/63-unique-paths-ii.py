class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return 0
        m,n = len(grid),len(grid[0])
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=1:
                    dp[j+1]+=dp[j]
                else:
                    dp[j+1] = 0
        return dp[-1]
        
                    
                
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        
        Dir = [0, 1, 0, -1, 0]
        
        def dfs(x, y):
            if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            for d in range(4):
                i, j = x+Dir[d], y+Dir[d+1]
                dfs(i, j)
        
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        
        return ans
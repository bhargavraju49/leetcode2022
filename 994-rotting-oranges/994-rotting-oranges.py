class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time = 0
        dp = [[sys.maxsize for i in range(n)] for i in range(m)]
        def bfs(i, j):
            q = [[i, j]]
            D = [[1, 0], [0, 1],[-1,0],[0,-1]]
            t = 1
            visited = [[i,j]]
            while q:
                _l = len(q)
                for i in range(_l):
                    _p = q.pop(0)
                    for a, b in D:
                        x = a + _p[0]
                        y = b + _p[1]
                        if x < m and y < n and x >= 0 and y >= 0 and [x,y] not in visited:
                            visited.append([x,y])
                            if grid[x][y] == 1:
                                q.append([x, y])
                                dp[x][y] = min(dp[x][y], t)
                            else:
                                dp[x][y] = 0
                t += 1
        rotten = True
        fresh = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dp[i][j] = 0
                if grid[i][j]==1 and fresh==False:
                    fresh = True
                if grid[i][j] == 2:
                    rotten = False
                    dp[i][j] = 0
                    bfs(i, j)  # send and update the vals
        if rotten == True and fresh== False:
            return 0
        if rotten == True and fresh == True:
            return -1
            
        mex = sys.maxsize*-1
        for i in range(m):
            for j in range(n):
                mex = max(dp[i][j],mex)

        if mex<sys.maxsize:
            return mex
        else:
            return -1
        
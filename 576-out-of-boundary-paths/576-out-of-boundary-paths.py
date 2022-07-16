class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        t = [[[-1 for _ in range(51)] for l in range(51)] for i in range(51)]
        def dfs_memoize(m,n,maxMove,sr,sc):
            if sr>=m or sr<0 or sc>=n or sc<0:
                return 1
            if maxMove<=0:
                return 0
            if t[sr][sc][maxMove]!= -1:
                return t[sr][sc][maxMove]
            
            result = 0
            result+= dfs_memoize(m,n,maxMove-1,sr-1,sc)
            result+= dfs_memoize(m,n,maxMove-1,sr+1,sc)
            result+= dfs_memoize(m,n,maxMove-1,sr,sc-1)
            result+= dfs_memoize(m,n,maxMove-1,sr,sc+1)
            t[sr][sc][maxMove] = result
            return t[sr][sc][maxMove]%1000000007
        
        return dfs_memoize(m,n,maxMove,startRow,startColumn)%1000000007
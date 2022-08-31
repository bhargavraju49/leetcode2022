class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n=len(heights)
        m=len(heights[0])
        
        if n==1 and m==1 and heights[n-1][m-1]>=1:
            return [[0,0]]
        
        ans=[]
        
        rVector=[-1, 0, 1, 0]
        cVector=[0, 1, 0, -1]
        
        pacific=[[0]*m for i in range(n)]
        atlantic=[[0]*m for i in range(n)]
        
        def checkPacific(r, c, pacific, prev):
            if r<0 or r>n-1 or c<0 or c>m-1:
                return
            if heights[r][c]<prev:
                return
            if pacific[r][c]:
                return
            pacific[r][c]=1
            for i in range(4):
                row=r+rVector[i]
                col=c+cVector[i]
                checkPacific(row, col, pacific, heights[r][c])
        
        def checkAtlantic(r, c, atlantic, prev):
            if r<0 or r>n-1 or c<0 or c>m-1:
                return
            if heights[r][c]<prev:
                return
            if atlantic[r][c]:
                return
            atlantic[r][c]=1
            for i in range(4):
                row=r+rVector[i]
                col=c+cVector[i]
                checkAtlantic(row, col, atlantic, heights[r][c])
            return
        
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    checkPacific(i, j, pacific, 0)
                if i==n-1 or j==m-1:
                    checkAtlantic(i, j, atlantic, 0)
        
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i,j])
        
        return ans
        
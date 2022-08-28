class Solution:
    def diagonalSort(self, m: List[List[int]]) -> List[List[int]]:
        if len(m)==1:
            return m
        m1,n = len(m),len(m[0])
        print(m1,n)
        for i in range (0,m1):
            s = []
            k = []
            row = i
            col = 0
            while row < m1 and col<n:
                s.append(m[row][col])
                k.append((row,col))
                col+=1
                row+=1
            s.sort()
            x = 0
            for r,c in k:
                m[r][c] = s[x]
                x+=1
        for i in range (1,n):
            s = []
            k = []
            row = 0
            col = i
            while row < m1 and col<n:
                s.append(m[row][col])
                k.append((row,col))
                col+=1
                row+=1
            s.sort()
            x = 0
            for r,c in k:
                m[r][c] = s[x]
                x+=1
        return m
            
            
                
                
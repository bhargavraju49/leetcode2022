class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix)
        cols = len(matrix[0])
        op = []
        
        r = 0
        c = 0
        
        i1 = 0
        start = 0
        end1 = cols
        end2 = rows
        
        while (i1<rows*cols):
            if (i1<rows*cols):
            # right traversal
                for i in range(start, end1):
                    op.append(matrix[r][i])
                    i1+=1
                    c = i
            if (i1<rows*cols):
            # down traversal
                for i in range(start+1,end2):
                    op.append(matrix[i][c])
                    i1+=1
                    r = i
            if (i1<rows*cols):
                # left traversal
                for i in range(end1-2,start-1,-1):
                    op.append(matrix[r][i])
                    i1+=1
                    c = i
            if (i1<rows*cols):
                # up traversal
                for i in range(end2-2,start,-1):
                    op.append(matrix[i][c])
                    i1+=1
                    r = i
            
            start+=1
            end1-=1
            end2-=1
            
        return op
                
        
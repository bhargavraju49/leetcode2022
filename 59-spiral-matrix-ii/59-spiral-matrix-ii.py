class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for i in range(n)]
        n1 = 1
        c = 1

        start= 0
        end = n

        while (c<=n*n):
            if n1 == 1:
                row = start
                for i in range(start,end):
                    matrix[row][i] = c
                    c+=1
                n1=2
            elif n1 == 2:
                col = end-1
                for i in range(start+1,end):
                    matrix[i][col] = c
                    c+=1
                n1=3

            elif n1 == 3:
                row = end-1
                for i in range(end-2,start-1,-1):
                    matrix[row][i] = c
                    c+=1
                n1=4
            elif n1 == 4:
                col = start
                for i in range(end-2,start,-1):
                    matrix[i][col] = c
                    c+=1
                start = start + 1
                end = end - 1
                n1 = 1
        return matrix
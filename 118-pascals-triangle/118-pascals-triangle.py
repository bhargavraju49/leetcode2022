class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        elif n==2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        
        for i in range(2,n):
            k = [1]
            
            for j in range(0,i-1):
                k.append(res[i-1][j]+res[i-1][j+1])
            
            k.append(1)
            res.append(k)
        return res
            
        
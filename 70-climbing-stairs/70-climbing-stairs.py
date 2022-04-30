class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        x = 1
        y = 2
        
        for i in range(2,n):
            y = x+y
            x = y-x
        
        return y
        

            
            
        
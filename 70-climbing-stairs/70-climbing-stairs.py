class Solution:
    def climbStairs(self, n: int) -> int:
        
        x,y = 1,1
        
        for i in range(2,n+1):
            y = x+y
            x = y-x
        
        return y
        

            
            
        
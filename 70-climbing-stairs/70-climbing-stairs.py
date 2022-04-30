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
        
        
#         def helper(n, c):     Recursion fails due to TLE
#             if n==0:
#                 c+=1
#                 return c
#             if n<0:
#                 return c
            
#             x = helper(n-1,c)
#             y = helper(n-2,c)
            
#             return x + y
            
#         return (helper(n,0))
        
#         1 - 1
#         2 - 2
#         3 - 3
#         4 - 3 + 2
#         5 - 5 + 3

            
            
        
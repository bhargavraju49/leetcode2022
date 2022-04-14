class Solution:
    def reverse(self, x: int) -> int:
        a =1 
        if x<0:
            a= -1
            
        y = abs(x)
        res = 0
        while y > 0:
            rem = y%10
            res = res*10 + rem
            y = y//10
        
        res = a*res
        if res > (2**31-1) or res < -(2**31):
            return 0
        
        return res
        
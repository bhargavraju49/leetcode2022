class Solution:
    def fib(self, n: int) -> int:
        f = 0
        s = 1
        while(n>0):
            k = f+s
            f = s
            s = k
            n=n-1
        return f
            
            
        
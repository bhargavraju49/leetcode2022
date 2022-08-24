class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        c=n
        while c>0:
            c=c/3
            if c==1 or n==1:
                return True   
        else:
            return False
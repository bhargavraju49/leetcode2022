class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0:
            k = bin(n)[2:]
            return k.count('1')==1
        else:
            return False
        
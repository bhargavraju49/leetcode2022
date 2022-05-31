class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        dp = set()
        for i in range(0,len(s) - k + 1):
            k1 = s[i:i+k]
            n = int(k1,2)
            if n<2**k:
                dp.add(n)
            if len(dp)==2**k:
                return True
        
        return False
    
            
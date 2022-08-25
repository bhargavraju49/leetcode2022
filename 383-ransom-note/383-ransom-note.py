class Solution:
    def canConstruct(self, a: str, b: str) -> bool:
        k = {}
        k2 = {}
        
        for i in a:
            k[i]=k.get(i,0)+1
            
        for i in b:
            k2[i]=k2.get(i,0)+1
            
        for i in a:
            if k[i]>k2.get(i,0):
                return False
        
        return True
        
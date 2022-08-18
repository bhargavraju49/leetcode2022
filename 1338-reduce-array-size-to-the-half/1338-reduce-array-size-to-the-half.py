class Solution:
    def minSetSize(self, a: List[int]) -> int:
        
        k = {}
        for i in a:
            k[i] = k.get(i,0)+1
        
        s = []
        k1 = len(a)
        for i in k:
            s.append(k[i])
        
        s.sort(reverse=True)
        
        res = 0
        
        for i,j in enumerate(s):
            res+=j
            
            if res>=k1/2:
                return i+1
        
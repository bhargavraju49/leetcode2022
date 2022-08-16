class Solution:
    def firstUniqChar(self, s: str) -> int:
        k = {}
        
        for i in range(len(s)):
            k[s[i]] = [i,k.get(s[i],[0,0])[1]+1]
            
        for i in k:
            if k[i][1] == 1:
                return k[i][0]
        
        return -1
        
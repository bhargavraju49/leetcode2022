class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map=[0]*26
        
        for i in s1:
            k=ord(i)-97
            s1map[k]=s1map[k]+1
        for i in range(len(s2)-len(s1)+1):
            s2map=[0]*26
            s=s2[i:len(s1)+i]
            for j in s:
                k=ord(j)-97
                s2map[k]=s2map[k]+1
            if s1map == s2map:
                return True
        return False
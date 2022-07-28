class Solution:
    def isAnagram(self, q: str, t: str) -> bool:
        if len(t)<len(q):
            return False
        
        f = {}
        s = {}
        for i in q:
            f[i] = f.get(i,0) + 1
        for i in t:
            s[i] = s.get(i,0) + 1
        print(f,s)
        for i in s.keys():
            k = f.get(i,0)
            print(s[i],k)
            if s[i]>k:
                return False
        return True
        
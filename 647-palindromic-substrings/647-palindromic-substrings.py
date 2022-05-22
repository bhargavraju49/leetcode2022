class Solution:
    def countSubstrings(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        while right < len(s):
            while right<len(s) and s[right] == s[left]:
                right+=1
            res += ((right-left)*(right-left+1))//2   #window slide accumilation == sum of n terms
            nleft = left-1
            nright = right
            while nleft>=0 and nright<len(s) and s[nleft]==s[nright]:
                res+=1
                nleft-=1
                nright+=1
            left = right
        return res
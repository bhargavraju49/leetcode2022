class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        i=0
        while i<len(s):

            center = i
            left = center-1
            right = center+1
            l=0
            while(left>=0 and right<len(s)):
                if s[left]!=s[right]:
                    break
                else:
                    l+=1
                left-=1
                right+=1
            
            if i+1<len(s) and s[i]==s[i+1]:
                left = i-1
                right = i+2
                l+=1
            while(left>=0 and right<len(s)):
                if s[left]!=s[right]:
                    break
                else:
                    l+=1
                left-=1
                right+=1
            res+=l
            i+=1
        res+=len(s)
        return res
            
        pass
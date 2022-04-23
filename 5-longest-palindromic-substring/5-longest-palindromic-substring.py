class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper (s):
            return s == s[::-1]
        
        if len(s) == 1:
            return s
        maxl = 0
        res=''

        for i in range(len(s)):
            start = i
            end = len(s)-1
            while start<end:
                if s[start] == s[end] and helper(s[start:end+1]):
                    l = end+1-start
                    if l> maxl:
                        maxl = l
                        res = s[start:end+1]
                    break
                end-=1	
        if res=='':
            return s[-1]
        return res
        pass



            
                
            
            
        
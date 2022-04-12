class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s):
            return s == s[::-1]
        start = 0
        end = len(s) - 1
        
        while start<end:
            x1 = False
            x2 = False
            if s[start] != s[end]:
                if s[start+1] == s[end]:
                    x1 = helper(s[start+1:end+1])
                if s[start] == s[end-1]:
                    x2 = helper(s[start:end])

                return x1 or x2
                
            else:
                start+=1
                end-=1
        return True
    

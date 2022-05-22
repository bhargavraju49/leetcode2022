class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        r = len(s)-1
        s = list(s)
        
        
        def helper(l):

            if l > r:
                res.append("".join(s))
                return
            
            if s[l].isalpha():
                s[l] = s[l].swapcase()
                helper(l+1)
                s[l] = s[l].swapcase()
            helper(l+1)
        
        helper(0)
        
        return res
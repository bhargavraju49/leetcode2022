class Solution:
    def removeDuplicates(self, s: str) -> str:
        if s == '':
            return ''
        stack = []

        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        res = ''
        for i in stack:
            res+=i
        
        return res
        
        
        
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(s):
            stack = []
            for i in s:
                if i == '#' and len(stack)>0:
                    stack.pop()
                elif i!='#':
                    stack.append(i)
            return stack
        
        return helper(s)==helper(t)
            
        
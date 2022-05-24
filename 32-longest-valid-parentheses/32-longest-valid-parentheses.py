class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s=='':
            return 0
        stack = []
        
        for i,j in enumerate(s):
            if j == '(':
                stack.append((i,'('))
            if j==')':
                if stack and stack[-1][1] == '(':
                    stack.pop()
                else:
                    stack.append((i,')'))
        if not stack:
            return len(s)
        stack.append((len(s),'#'))
        maxc = 0
        prev = -1
        for i,j in stack:
            maxc = max(maxc, i-prev-1)
            prev = i
        
        return maxc
            
                    
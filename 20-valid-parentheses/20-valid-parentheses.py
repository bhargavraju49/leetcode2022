class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i == '(' or i == '[' or i =='{':
                stack.append(i)
            else:
                if not stack:
                    return False
                check = stack.pop()
                # print(check)
                if (i == ')' and check != '(') or (i == ']' and check != '[') or ( i=='}' and check != '{'):
                    return False
                
        return len(stack)==0
        
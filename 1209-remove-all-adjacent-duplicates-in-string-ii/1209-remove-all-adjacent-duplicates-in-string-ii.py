class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
#         def checkstring(s):
#             k=s[0]
#             for i in s:
#                 if i!=k:
#                     return False
#             return True
                
#         def helper(s,k):
#             if len(s)==0 or len(s)==1:
#                 return s
#             elif len(s)==k and checkstring(s):
#                 return ""
#             elif len(s)==k and not checkstring(s):
#                 return s
            
#             for i in range(len(s)-k):
#                 if checkstring(s[i:i+k]):
#                     return helper(s[:i]+s[i+k:],k)
                
#             return s
#         if len(s)==0 or len(s)==1:
#             return s
#         elif len(s)==k and checkstring(s):
#             return ""
#         elif len(s)==k and not checkstring(s):
#             return s
        
#         return helper(s+' ',k)[:-1]  # TLE
        stack = [] # to store 2d array with char and rep
        
        for i in range(len(s)):
            if stack and stack[-1][0] == s[i]:
                if stack[-1][1] != k-1 :
                    stack[-1][1] += 1
                else:
                    stack.pop()
            else:
                stack.append([s[i],1])
               
        ans = ''
        for i in stack:
            ans += i[0]*i[1]
            
        return ans
                
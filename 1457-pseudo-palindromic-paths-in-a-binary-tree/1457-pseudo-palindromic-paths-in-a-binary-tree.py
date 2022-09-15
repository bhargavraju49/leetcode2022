# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        freq = [0 for _ in range(10)]
        res = 0
        
        def isPalindrome():
            count_odd = 0
            for i in range(10):
                if freq[i] % 2:
                    count_odd += 1
            
            return False if count_odd > 1 else True
            
        
        def dfs(node):
            
            nonlocal res
            
            if not node:
                return
            
            freq[node.val] += 1
            
            if not node.left and not node.right:
                if isPalindrome():
                    res += 1
            else:
                dfs(node.left)
                dfs(node.right)
            
            freq[node.val] -= 1
            
        
        dfs(root)
        
        return res
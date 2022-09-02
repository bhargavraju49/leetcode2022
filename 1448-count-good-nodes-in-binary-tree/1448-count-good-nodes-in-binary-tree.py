# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = [0]
        def counter (root, m):
            if not root:
                return
            
            if root.val>=m:
                res[0]+=1
                
            ml = m
            mr = m
            if root.left:
                ml = max(m,root.left.val)
            if root.right:
                mr = max(m,root.right.val)
                
            l = counter(root.left,ml)
            r = counter(root.right,mr)
            
            return
        
        counter(root, root.val)
        
        return res[0]
            
            
            
            
        
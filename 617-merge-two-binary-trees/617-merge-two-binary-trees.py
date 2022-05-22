# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(t1,t2):
            if t1 is None:
                return t2
            if t2 is None:
                return t1
            
            t1.val+=t2.val
            
            t1.left = helper(t1.left, t2.left)
            t1.right = helper(t1.right, t2.right)
            
            return t1
            pass
        
        return helper(t1,t2)
        
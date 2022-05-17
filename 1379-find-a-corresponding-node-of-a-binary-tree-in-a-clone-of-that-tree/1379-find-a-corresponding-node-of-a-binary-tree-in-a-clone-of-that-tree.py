# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def helper(root,clone,target):
            if root is None:
                return 
            if root == target:
                return clone
                
            l = helper(root.left,clone.left,target)
            r = helper(root.right,clone.right,target)
            
            if l is not None:
                return l
            if r is not None:
                return r

        
        return helper(original,cloned,target)
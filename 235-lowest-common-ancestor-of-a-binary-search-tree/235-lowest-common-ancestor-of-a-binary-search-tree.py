# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(root,p,q):
            
            if (p>root.val and q>root.val):
                return helper(root.right,p,q)
                
            elif (p<root.val and q<root.val):
                return helper(root.left,p,q)
            else:
                return root

        
        return helper(root,p.val,q.val)
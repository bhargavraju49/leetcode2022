# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def t(node,s):
            if not node:
                return ''
            elif node.left is None and node.right is None:
                return str(node.val)
            elif node.right is None:
                s+=str(node.val)+'('+t(node.left,s)+')'
            
            else:
                s+=str(node.val)+'('+t(node.left,s)+')('+t(node.right,s)+')'
            return s
        
        return t(root,"")
        
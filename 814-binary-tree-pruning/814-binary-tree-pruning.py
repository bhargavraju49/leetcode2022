# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return True
            
            l = helper(root.left)
            r = helper(root.right)
            # print(root.val,l,r)
            if not root.left and not root.right:
                if l and r and root.val == 0:
                    return True
                else:
                    return False
            else:
                if l:
                    root.left = None
                if r:
                    root.right = None
                if l and r and root.val == 0:
                    return True
                else:
                    return False
                 
        
        k = helper(root)
        if not k:
            return root
        else:
            return None
        
        
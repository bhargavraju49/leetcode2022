# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.v = 0
        def helper(root,k):
            if root is None:
                return 
            l = helper(root.left,k)
            if l is not None:
                return l
            self.v +=1
            if self.v == k:
                return root.val
            r = helper(root.right,k)
            if r is not None:
                return r

        return helper(root,k)

            
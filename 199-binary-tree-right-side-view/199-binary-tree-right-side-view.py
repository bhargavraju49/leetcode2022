# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        res = []
        
        while q:
            if q[-1] is not None:
                res.append(q[-1].val)
            q2 = []
            for i in q:
                if i:
                    if i.left is not None:
                        q2.append(i.left)
                    if i.right is not None:
                        q2.append(i.right)
            q = q2
        return res
        
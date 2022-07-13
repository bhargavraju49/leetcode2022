# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = [[root.val]]
        q = [root]
        
        while q:
            q2 = []
            re = []
            for i in q:
                if i.left:
                    q2.append(i.left)
                    re.append(i.left.val)
                if i.right:
                    q2.append(i.right)
                    re.append(i.right.val)
            q=q2
            if re:
                res.append(re)
        return res
                
        
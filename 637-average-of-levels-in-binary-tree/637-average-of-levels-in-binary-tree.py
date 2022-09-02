# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        q = [root]
        res = [root.val]
        while q:
            
            q2 = []
            s = 0
            for i in q:
                if i.left:
                    q2.append(i.left)
                    s+=i.left.val
                if i.right: 
                    q2.append(i.right)
                    s+=i.right.val
            
            q = q2
            if len(q)>0:
                s = s/len(q)
                res.append(s)
        return res
        
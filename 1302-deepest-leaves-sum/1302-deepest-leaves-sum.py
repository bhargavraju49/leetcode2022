# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        #####
        #DFS#
        #####
        
        
#         def helper(root):
#             if  root is None:
#                 return 0
#             l = 1 + helper(root.left)
#             r = 1 + helper(root.right)
#             return max(l,r)
#         height = helper(root)
        
#         def counter(root,h):
#             if  root is None:
#                 return 0
#             l = counter(root.left,h-1)
#             r = counter(root.right,h-1)
#             if h==1:
#                 return root.val
#             return l+r
        
#         k = counter(root,height)
#         return k
        
        #####
        #BFS#
        #####
        
        q = [root]
        count = 0
        while q:
            it = len(q)
            summ = 0
            for i in range(it):
                node = q.pop(0)
                summ+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if summ:
                count=summ
        return count
            
                
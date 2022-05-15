# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        sum1 = root.val
        
        while q:
            l = len(q)
            tempsum = 0
            
            for i in range(l):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    tempsum+=node.left.val
                if node.right:
                    q.append(node.right)
                    tempsum+=node.right.val
            if tempsum:
                sum1 = tempsum
        
        return sum1

                
                
            
            
                    
        
            
                
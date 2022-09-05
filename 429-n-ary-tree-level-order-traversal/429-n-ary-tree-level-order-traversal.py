"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = [root]
        res = []
        
        while q:
            q2 = []
            o = []
            for i in q:
                if i:
                    o.append(i.val)
            res.append(o)
            
            for i in q:
                if i:
                    k = i.children
                    q2+=k
            
            q = q2
                
        return res
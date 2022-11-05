"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def helper(node,array):
            if not node:
                return
            
            array.append(node.val)
            for child in node.children:
                helper(child,array)
                
            return array
            pass
        
        return helper(root,[])
        
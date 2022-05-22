"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(root):
            if root is None:
                return
            q = [root]
            while q:
                l = len(q)
                prev = None
                for i in range(l):
                    k = q.pop(0)
                    if prev is not None:
                        prev.next = k.left

                    if k.left is not None:
                        k.left.next = k.right
                        prev = k.right
                        q.append(k.left)
                        q.append(k.right)


        helper(root)
        return root
    
        
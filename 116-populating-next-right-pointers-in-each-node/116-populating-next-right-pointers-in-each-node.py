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
                for i in range(l):
                    k = q.pop(0)
                    if k.left is not None:
                        q.append(k.left)
                        q.append(k.right)

                for i in range(len(q)-1):
                    q[i].next=q[i+1]

        helper(root)
        return root
    
        
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
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while(head!=None):
            #print("head",head.val)
            if head.left:
                prev = head.left
            elif head.right:
                prev = head.right
            else:
                head = head.next
                continue
            p = head
            while(p!=None and prev!= None):
                #print(prev,p.val)
                if p.left != None:
                    prev.next = p.left
                    p.left.next = p.right
                    if p.right == None:
                        prev = p.left
                    else:
                        prev = p.right
                elif p.right:
                    if p.right != prev:
                        prev.next = p.right
                        prev = p.right
                p=p.next
            if head.left:
                head = head.left
            else:
                head = head.right
        return root
        
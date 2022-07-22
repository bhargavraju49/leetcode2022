# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None                    
        less, more = ListNode(), ListNode()
        lNode, mNode = less, more
        
        while head :                                              
            if head.val < k :
                lNode.next = head
                lNode = lNode.next
            else:
                mNode.next = head
                mNode = mNode.next
            head=head.next

        lNode.next, mNode.next = more.next, None   

        return less.next           
        
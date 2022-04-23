# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        dummy = ListNode (1)
        slow = dummy
        dummy.next = fast
        x = 0
        while (x<n-1):
            fast = fast.next
            x+=1
        while(fast.next):
            slow = slow.next
            fast=fast.next
        
        slow.next = slow.next.next
    
        return dummy.next
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        while fast and fast.next: #fast is jumping 2x amd slow in jumping 1x when slow reaches mid fast complete track
            fast =fast.next.next
            slow=slow.next
        return slow
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
                
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        elif l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1

#         head1 = l1
#         head2 = l2
#         prev = None

        
#         while (head1 and head2):
#             if head1.val < head2.val:
#                 prev = head1
#                 head1 = head1.next
#             else:
#                 if prev:
#                     prev.next = head2
                
#                 prev = head2
#                 head2 = head2.next
#                 prev.next = head1
        
#         if not head1:
#             prev.next = head2
        
#         if l1.val < l2.val:
#             return l1
#         else:
#             return l2
    
            
        
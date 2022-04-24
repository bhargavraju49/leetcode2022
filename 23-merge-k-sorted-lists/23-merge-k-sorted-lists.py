# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) < 2:
            return lists[0]
        
        def helper (l1,l2):
            if l1 is None:
                return l2
            if l2 is None:
                return l1

            if l1.val <= l2.val:
                l1.next = helper(l1.next, l2)
                return l1
            elif l1.val > l2.val:
                l2.next = helper(l1,l2.next)
                return l2
        
        
        for i in range(len(lists) - 1):
            l1 = lists[i]
            l2 = lists[i+1]
            merged = helper(l1,l2)
            lists[i+1] = merged
        
        
        return lists[-1]

            
        
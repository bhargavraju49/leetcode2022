class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head, prev):
            if not head:
                return prev
            nxt = head.next
            head.next = prev
            return rev(nxt, head)
            
        return rev(head, None)
        
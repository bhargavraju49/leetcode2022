# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        while head is not None:
            a.append(head.val)
            head = head.next
        x = 0
        y = len(a)-1
        
        while x<=y:
            if a[x]!=a[y]:
                return False
            else:
                x+=1
                y-=1
        return True
        
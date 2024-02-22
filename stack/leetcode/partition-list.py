# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessthan = ListNode() 
        greater = ListNode()
        s = lessthan
        l = greater
    
        while head:
            if head.val < x:
                lessthan.next = head
                lessthan = lessthan.next
                head = head.next
                lessthan.next = None

            else:
                greater.next = head
                greater = greater.next
                head = head.next
                greater.next = None
            
            
        lessthan.next = l.next
        return s.next
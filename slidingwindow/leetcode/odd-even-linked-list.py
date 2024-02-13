# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1 
        tail = head
        prev = head
        while tail and tail.next:
            prev = tail
            tail = tail.next
            length += 1
        
        
        mid =(length//2) 
        if length <= 2:
            return head

       
        start = head
        while mid > 0 and start:
            temp = start.next
            start.next = start.next.next
            temp.next = None
            tail.next = temp
            tail = tail.next
            start = start.next
            mid -= 1
        return head




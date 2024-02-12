# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head

        for i in range(1,n+1):
            right = right.next

        if right == None:
            return head.next
            
        while right.next != None:
            right = right.next
            left = left.next

        left.next = left.next.next

        return head

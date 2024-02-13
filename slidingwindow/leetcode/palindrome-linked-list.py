# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
         
        prev = slow
        curr = slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        ptr= head
        curr = prev
        while ptr != slow:
            if ptr.val == curr.val:
                ptr = ptr.next
                curr = curr.next
            else:
                return False
        return True
         
         
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        flag = False

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
                flag = True
            else:
                if flag:
                    prev.next = current.next
                    current = prev.next
                    flag = False
                else:
                    prev = current
                    current = current.next

        if flag:
            prev.next = current.next

        return dummy.next
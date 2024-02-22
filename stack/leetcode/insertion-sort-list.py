# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        dummy = ListNode(0)  
        dummy.next = head
        current = head   

        while current.next:
            if current.val > current.next.val:
               
                prev = dummy
                while prev.next.val < current.next.val:
                    prev = prev.next

                # Insert the current.next node in its correct position
                temp = current.next
                current.next = temp.next
                temp.next = prev.next
                prev.next = temp
            else:
                # If the next node is greater, move to the next node
                current = current.next

        return dummy.next  
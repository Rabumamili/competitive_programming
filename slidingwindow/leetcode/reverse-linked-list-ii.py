# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None, size = 1):
#         self.val = val
#         self.next = next
#         self.size = size

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
    #   Traverse to the node at position left - 1
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

    # Keep references to the nodes at position left - 1 and left
        left_node = prev.next
 
        curr = left_node
        next_node = None
        prev_node = None
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
    # Update the next pointer of the node at position left - 1
        prev.next = prev_node
          
        left_node.next = curr
        return dummy.next
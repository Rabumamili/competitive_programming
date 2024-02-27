# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
 
        # Base case: empty list or single node
        if not head or not head.next:
            return head

        # Swap the current node and the next node
        next_node = head.next
        head.next = self.swapPairs(next_node.next)
        next_node.next = head

        # Set the head to the next node
        return next_node
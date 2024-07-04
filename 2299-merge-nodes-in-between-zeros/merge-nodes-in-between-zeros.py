class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, next_node = head, head.next
        while next_node.next:
            if next_node.val:
                node.val += next_node.val
            else:
                node = node.next
                node.val = 0              
            next_node = next_node.next
        node.next = None
        return head